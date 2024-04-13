from typing import Iterator, Optional

from .repositories import ProductRepository
from .schemas import (Product as ProductSchema)
from src.product.models import Product


class ProductService:

    def __init__(self, product_repository: ProductRepository) -> None:
        self._repository: ProductRepository = product_repository

    def get_product(self) -> Iterator[Product]:
        return self._repository.get_all()

    def get_product_by_id(self, product_id: int) -> Product:
        return self._repository.get_by_id(product_id)

    def create_product(self, product_schema: ProductSchema) -> Product:
        return self._repository.add(product_schema=product_schema)
    
    def update_product(self, product_id: int, update_product: ProductSchema) -> Product:
        return self._repository.patch(product_id=product_id, update_product=update_product)

    def delete_product_by_id(self, product_id: int) -> None:
        return self._repository.delete_by_id(product_id)