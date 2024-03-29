## redo

from pydantic import BaseModel

#like serializer
class Book(BaseModel):
    title: str
    rating: int
    author_id: int

    class Config:
        orm_mode = True


class Author(BaseModel):
    name: str
    age: int

    class Config: 
        orm_mode = True