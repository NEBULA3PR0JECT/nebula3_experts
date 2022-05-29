from dataclasses import dataclass
from .defines import OutputStyle

@dataclass
class ExpertParam:
    movie_id: str
    scene_element: int = None
    local: bool = False
    extra_params: dict = None
    output: str = OutputStyle.DB


