from typing import Optional
from fastapi import FastAPI

tags_metadata = [
    {
        "name": "status",
        "description": "View running status of pipeline steps.",
    },
    {
        "name": "set",
        "description": "Set a configuration: <cfg_name>=<value> where cfg_name is one of the configurations \
        run 'cfg' command to see possible configurations.",
    },
    {
        "name": "cfg",
        "description": "list all editable configurations.",
    },
]

app = FastAPI(openapi_tags=tags_metadata)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/status")
def get_status(q: Optional[str] = None):
    return {"status": "running" }

@app.post("/set}", tags=['set'] )
def post_status(q: Optional[str] = None):
    return {"set": 'ok', "q": q }

@app.get("/cfg}", tags=['cfg'] )
def get_config(q: Optional[str] = None):
    return {"set": 'ok', "q": q }

