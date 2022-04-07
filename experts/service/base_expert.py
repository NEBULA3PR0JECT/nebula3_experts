from abc import ABC, abstractmethod
from fastapi import FastAPI

class BaseExpert:


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


