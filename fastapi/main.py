from typing import Optional
from fastapi import FastAPI, status, Response, HTTPException
from fastapi.params import Body
from pydantic import BaseModel

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


@app.get("/")
def root():
    return {"data" : "Hello, World"}

@app.get("/posts")
def get_posts():
    return {"data" : posts}

# by default 200 is sent if everything is ok to change that we use the status_code argument
# 201 is used to indicated something has been successfully created
@app.get("/post/{id}", status_code=status.HTTP_201_CREATED)
def get_post(id : int, response : Response):
    try:
        if id < 0 or id >= len(posts):
            response.status_code = 404
            return {"message" : "invalid id"}
        else:
            for i in range(len(posts)):
                if posts[i]["id"] == id:
                    return {"data" : posts[i]}
            return {"message" : f"post with id = {id} not found"}
    except Exception as e:
        print(e)
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"post with id = {id} not found")
    
@app.post("/create-post")
def create_post(new_post : Post):
    #pydantic automatically extracts the data 
    print(new_post)
    print(new_post.title)
    print(new_post.content)
    # to convert pydantic model to a dictionary 
    post_dct = new_post.model_dump()
    post_dct.update({"id" : len(posts)})
    print(f"new post = {post_dct}")
    posts.append(new_post)
    return {"data" : new_post}

@app.delete("/delete-post/{id}")
def delete_post(id : int, response : Response):
    if id < 0 or id >= len(posts):
        response.status_code = 404
        return {"message" : "invalid id"}
    else:
        for i in range(len(posts)):
            if posts[i]["id"] == id:
                del posts[i]
                return {"message" : "post deleted"}
        return {"message" : f"post with id = {id} not found"}

    
