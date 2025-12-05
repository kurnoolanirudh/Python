from typing import Optional
from fastapi import FastAPI, status, Response, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor # used to get column names along with the results from the db
import time
from .schema import Post, CreatePost, CreatePostResponse, UpdatePost


app = FastAPI()

# dummy in memory data for testing
posts = [
    {
        "id" : 0,
        "title" : "post1",
        "content" : "a test post",
    },

    {
        "id" : 1,
        "title" : "post2",
        "content" : "a test post",
    },

    {
        "id" : 2,
        "title" : "post3",
        "content" : "a test post",
    },
]

class Post(BaseModel):
    title       : str
    content     : str               # default values 
    published   : bool            = True 
    rating      : Optional[int]   = None 

# connecting to the database
while True: # sometimes connection to db may fail for some unknown reason so to keep retrying until a successful connection
    try:
        conn = psycopg2.connect(host="localhost", database="SOCIAL_MEDIA", user="postgres", password="password", cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("connected to database successfully")
        break
    except Exception as error:
        print("connection to database failed")
        print(f"error : {error}")
        print(f"sleeping for 10 seconds before retrying to connect again")
        time.sleep(10)
        


@app.get("/")
def root():
    return {"data" : "Hello, World"}

@app.get("/posts")
def get_posts():
    cursor.execute(""" SELECT * FROM public."POSTS" """)
    posts = cursor.fetchall()
    return {"data" : posts}


@app.get("/post/{id}")
def get_post(id : int, response : Response):
    try:
        # if id < 0 or id >= len(posts):
        #     response.status_code = 404
        #     return {"message" : "invalid id"}
        # else:
        #     for i in range(len(posts)):
        #         if posts[i]["id"] == id:
        #             return {"data" : posts[i]}
        #     return {"message" : f"post with id = {id} not found"}

        cursor.execute(""" SELECT * FROM public."POSTS" WHERE "ID" = %s""", (str(id)))
        post = cursor.fetchone()
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id = {id} not found")
        return {"data" : post}
    except Exception as e:
        print(e)
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"post with id = {id} not found")
    
# by default 200 is sent if everything is ok to change that we use the status_code argument
# 201 is used to indicated something has been successfully created   
@app.post("/create-post", status_code=status.HTTP_201_CREATED)
def create_post(new_post : Post):
    #pydantic automatically extracts the data 
    # print(new_post)
    # print(new_post.title)
    # print(new_post.content)
    # to convert pydantic model to a dictionary 
    # post_dct = new_post.model_dump()
    # if len(posts) > 0:
    #     post_dct.update({"id" : (posts[-1]["id"] + 1)})
    # else:
    #     post_dct.update({"id" : 1})
    # print(f"new post = {post_dct}")
    # posts.append(post_dct)

    # never pass in data recieved from user directly into the SQL command using string interpolation(f strings ) 
    cursor.execute(""" INSERT INTO public."POSTS" ("TITLE", "CONTENT", "PUBLISHED") VALUES (%s, %s, %s) RETURNING * """, (new_post.title, new_post.content, new_post.published)) # this will santize user inputs 
    new_post = cursor.fetchone()
    conn.commit() # this is necessary when adding things to the DB
    return {"data" : new_post}

# by default 200 is sent if everything is ok to change that we use the status_code argument
# 204 is used to indicated something has been successfully deleted
@app.delete("/delete-post/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id : int, response : Response):
    cursor.execute("""DELETE FROM public."POSTS" WHERE "ID" = %s RETURNING *""", (str(id)))
    deleted_post = cursor.fetchone()
    conn.commit() #any time data is mutated in the DB this line should be added
    if not deleted_post:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"post with id = {id} not found")
    print({"deleted_post" : deleted_post})
    # else:
    #     for i in range(len(posts)):
    #         if posts[i]["id"] == id:
    #             del posts[i]
    #             return Response(status_code=status.HTTP_204_NO_CONTENT)
    #     # return {"message" : f"post with id = {id} not found"} # with 204 you're not supposed to send any data back
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id = {id} does not exist")
    

@app.put("/update-post-1/{id}")
def update_post_put(id : int, updated_post : Post):
    cursor.execute(""" UPDATE public."POSTS" SET "TITLE" = %s , "CONTENT" = %s , "PUBLISHED" = %s, "RATING" = %s WHERE "ID" = %s RETURNING * """, (updated_post.title, updated_post.content, updated_post.published ,updated_post.rating, str(id)))
    updated_post = cursor.fetchone()
    
    if not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post with id = {id} not found")
    
    conn.commit()
    return {"updated_post" : updated_post}
    # else:
    #     for i in range(len(posts)):
    #         if posts[i]["id"] == id:
    #             posts[i]["title"] = updated_post.title
    #             posts[i]["content"] = updated_post.content
    #             return {"data" : posts[i]}
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id = {id} does not exist")

# routes which use the ORM 


# from . import models # importing models.py 
# from .database import engine , db_session
# from sqlalchemy.orm import Session 
# from fastapi import Depends


# models.Base.metadata.create_all(bind=engine) # this line will persists all the models to the database 

# def get_db():
#     db = db_session()
#     try:
#         yield db 
#     finally:
#         db.close()

# @app.get("/posts-orm")
# def get_posts_orm(db : Session = Depends(get_db)):
#     return {"status":"success"}


    


    
