from typing import Callable, Iterator, Optional
from contextlib import AbstractContextManager

from sqlalchemy.orm import Session

from .models import Bahan
from .schemas import Bahan as BahanSchema, UpdateBahan

class BahanRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[Bahan]:
        with self.session_factory() as session:
            return session.query(Bahan).all()

    def get_by_id(self, bahan_id: int) -> Bahan:
        with self.session_factory() as session:
            bahan = session.query(Bahan).filter(Bahan.id == bahan_id).first()
            if not bahan:
                raise BahanNotFoundError(bahan_id)
            return bahan
    
    def add(self, bahan_schema: BahanSchema) -> Bahan:
        with self.session_factory() as session:
            bahan = Bahan(name=bahan_schema.name, description=bahan_schema.description)
            session.add(bahan)
            session.commit()
            session.refresh(bahan)
            return bahan
    
    def patch(self, bahan_id:int, update_bahan: UpdateBahan) -> Bahan:
        with self.session_factory() as session:
            bahan: Bahan = session.query(Bahan).filter(Bahan.id == bahan_id).first()
            if not bahan:
                raise BahanNotFoundError(update_bahan)
            
            update_data = {}
            if update_bahan.name is not None:
                update_data['name'] = update_bahan.name
            if update_bahan.description is not None:
                update_data['description'] = update_bahan.description

            bahan = session.merge(Bahan(id=bahan_id, **update_data))
            session.commit()
            session.refresh(bahan)

        return bahan

    def delete_by_id(self, bahan_id: int) -> None:
        with self.session_factory() as session:
            entity: Bahan = session.query(Bahan).filter(Bahan.id == bahan_id).first()
            if not entity:
                raise BahanNotFoundError(bahan_id)
            session.delete(entity)
            session.commit()




class NotFoundError(Exception):
    entity_name: str

    def __init__(self, entity_id):
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")


class BahanNotFoundError(NotFoundError):
    entity_name: str = "Bahan"