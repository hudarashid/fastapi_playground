from typing import Optional
from pydantic import BaseModel

class Bahan(BaseModel):
    name: str
    description: str


class UpdateBahan(Bahan):
    name: Optional[str] = None
    description: Optional[str] = None