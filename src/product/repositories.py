from typing import Callable, Iterator, Optional
from contextlib import AbstractContextManager

from sqlalchemy.orm import Session

from .models import Product
from .schemas import Product as ProductSchema

class ProductRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[Product]:
        with self.session_factory() as session:
            return session.query(Product).all()

    def get_by_id(self, product_id: int) -> Product:
        with self.session_factory() as session:
            product = session.query(Product).filter(Product.id == product_id).first()
            if not product:
                raise ProductNotFoundError(product_id)
            return product
    
    def add(self, product_schema: ProductSchema) -> Product:
        with self.session_factory() as session:
            product = Product(name=product_schema.name, description=product_schema.description, user_id=product_schema.user_id)
            session.add(product)
            session.commit()
            session.refresh(product)
            return product
    
    def patch(self, product_id:int, update_product: ProductSchema) -> Product:
        with self.session_factory() as session:
            product: Product = session.query(Product).filter(Product.id == product_id).first()
            if not product:
                raise ProductNotFoundError(update_product)
            
            update_data = {}
            if update_product.name is not None:
                update_data['name'] = update_product.name
            if update_product.description is not None:
                update_data['description'] = update_product.description
            if update_product.user_id is not None:
                update_data['user_id'] = update_product.user_id

            product = session.merge(Product(id=product_id, **update_data))
            session.commit()
            session.refresh(product)

        return product

    def delete_by_id(self, product_id: int) -> None:
        with self.session_factory() as session:
            entity: Product = session.query(Product).filter(Product.id == product_id).first()
            if not entity:
                raise ProductNotFoundError(product_id)
            session.delete(entity)
            session.commit()




class NotFoundError(Exception):
    entity_name: str

    def __init__(self, entity_id):
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")


class ProductNotFoundError(NotFoundError):
    entity_name: str = "Product"