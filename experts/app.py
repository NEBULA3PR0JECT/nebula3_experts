from typing import Optional
from fastapi import FastAPI
from .service.base_expert import BaseExpert
from nebula3_pipeline.pipeline.api import PipelineApi

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

class ExpertApp:
    def __init__(self, expert: BaseExpert, params = None):
        self.params = params
        self.expert = expert
        self.pipeline = PipelineApi()
        self.init_pipeline()
        self.app = FastAPI(openapi_tags=tags_metadata)
        self.add_base_apis()
        # Add expert specific apis
        self.expert.add_expert_apis(self.app)

    def init_pipeline(self):
        """init pipeline params
        and add pipeline event handlers/callbacks
        """
        self.pipeline.subscribe(self.expert.get_name(),
                                self.expert.get_dependency(),
                                self.on_pipeline_msg)

    def on_pipeline_msg(self, msg):
        self.expert.handle_msg(msg)


    def add_base_apis(self):
        """add base apis

        Returns:
            _type_: _description_
        """
        @self.app.get("/")
        def read_root():
            return {"Expert": self.expert.get_name()}


        @self.app.get("/status")
        def get_status(q: Optional[str] = None):
            return {"status": self.expert.get_status() }

        @self.app.post("/set}", tags=['set'] )
        def post_config(q: Optional[str] = None):
            return {"set": 'ok', "q": q }

        @self.app.get("/cfg}", tags=['cfg'] )
        def get_config(q: Optional[str] = None):
            return {"set": 'ok', "q": q }

    def run(self):
        print("Running...")
        # self.expert.run()

    def get_app(self):
        return self.app

