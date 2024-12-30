from pydantic import BaseModel
from typing import Union


class UpdateRequest(BaseModel):
    operation: str
    value: Union[int, float]
