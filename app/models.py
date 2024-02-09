from pydantic import BaseModel
from typing import List


class Visit(BaseModel):
    links: List[str]
