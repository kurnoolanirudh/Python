from typing import Optional
from pydantic import BaseModel

class Post(BaseModel):
    title       : str
    content     : str               # default values 
    published   : bool            = False 
    rating      : Optional[int]   = None 

class CreatePost(Post):
    pass 

# rather sending the post with the ID and Created_At timestamp this will only send title, content, publised and rating
class CreatePostResponse(Post):
    pass

class UpdatePost(Post):
    pass

