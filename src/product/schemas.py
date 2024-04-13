from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    user_id: Optional[int] = None


# class UpdateProduct(Product):
#     name: Optional[str] = None
#     description: Optional[str] = None