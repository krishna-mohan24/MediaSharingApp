from typing import Optional
from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate

app = FastAPI()

text_posts = {"1": {"title": "First Post", "content": "This is the first post."},
               "2": {"title": "Second Post", "content": "This is the second post."},
               "3": {"title": "Third Post", "content": "This is the third post."},
               "4": {"title": "Fourth Post", "content": "This is the fourth post."},
               "5": {"title": "Fifth Post", "content": "This is the fifth post."},
               "6": {"title": "Sixth Post", "content": "This is the sixth post."},
               "7": {"title": "Seventh Post", "content": "This is the seventh post."},
               "8": {"title": "Eighth Post", "content": "This is the eighth post."},
               "9": {"title": "Ninth Post", "content": "This is the ninth post."},
               "10": {"title": "Tenth Post", "content": "This is the tenth post."}
               }

@app.get("/posts")
def get_posts(limit: int = None):
    posts = list(text_posts.values())
    if limit:
        return posts[:limit]
    return text_posts

@app.get("/posts/{post_id}")
def get_post(post_id: str):
    if post_id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts[post_id]

# Request Body
# Since we are using pydantic, fastapi knows by default that this is request body
@app.post("/posts")
def create_post(post: PostCreate):
    new_id = str(max(int(k) for k in text_posts.keys()) + 1)
    text_posts[new_id] = {"title": post.title, "content": post.content}
    return text_posts[new_id]
