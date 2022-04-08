from abc import ABC, abstractmethod
from fastapi import FastAPI


from nebula3_pipeline.nebula3_database.movie_db import MOVIE_DB
from nebula3_pipeline.nebula3_database.movie_s3 import MOVIE_S3
from nebula3_pipeline.nebula3_database.movie_tokens import MovieTokens

class BaseExpert(ABC):
    def __init__(self):
        self.movie_db = MOVIE_DB()
        self.db = self.movie_db.db
        self.movie_s3 = MOVIE_S3()
        self.movie_tokens = MovieTokens(self.db)

    @abstractmethod
    def add_expert_apis(self, app: FastAPI):
        """add expert's specific apis (REST)

        Args:
            app (FastAPI): _description_
        """
        pass

    @abstractmethod
    def get_name(self) -> str:
        """return expert's name
        """
        pass

    @abstractmethod
    def get_dependency(self) -> str:
        """return the expert's dependency in the pipeline:
        which pipeline step is this expert depends on
        pass

        Returns:
            str: _description_
        """
    @abstractmethod
    def handle_msg(self):
        """ handle new msg (movies) """
        pass

