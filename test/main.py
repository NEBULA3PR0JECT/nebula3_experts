# from typing import Optional
from fastapi import FastAPI

# tags_metadata = [
#     {
#         "name": "status",
#         "description": "View running status of pipeline steps.",
#     },
#     {
#         "name": "set",
#         "description": "Set a configuration: <cfg_name>=<value> where cfg_name is one of the configurations \
#         run 'cfg' command to see possible configurations.",
#     },
#     {
#         "name": "cfg",
#         "description": "list all editable configurations.",
#     },
# ]

# app = FastAPI(openapi_tags=tags_metadata)

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/status")
# def get_status(q: Optional[str] = None):
#     return {"status": "running" }

# @app.post("/set}", tags=['set'] )
# def post_status(q: Optional[str] = None):
#     return {"set": 'ok', "q": q }

# @app.get("/cfg}", tags=['cfg'] )
# def get_config(q: Optional[str] = None):
#     return {"set": 'ok', "q": q }

from typing import Optional

from experts.service.base_expert import BaseExpert
from experts.app import ExpertApp

class MyExpert(BaseExpert):
    def __init__(self):
      super.__init__()


    def get_name(self):
        return "MyExpert"
    def get_status(self):
        return "MyExpert- running"
    def add_expert_apis(self, app: FastAPI):
        @app.get("/my-expert")
        def get_my_expert(q: Optional[str] = None):
            return {"expert": "my-expert" }

my_expert = MyExpert()
expert_app = ExpertApp(expert=my_expert)
app = expert_app.get_app()
expert_app.run()
