from typing import Iterator, Optional

from .repositories import BahanRepository
from .schemas import (Bahan as BahanSchema, UpdateBahan)
from src.bahan.models import Bahan


class BahanService:

    def __init__(self, bahan_repository: BahanRepository) -> None:
        self._repository: BahanRepository = bahan_repository

    def get_bahan(self) -> Iterator[Bahan]:
        return self._repository.get_all()

    def get_bahan_by_id(self, bahan_id: int) -> Bahan:
        return self._repository.get_by_id(bahan_id)

    def create_bahan(self, bahan_schema: BahanSchema) -> Bahan:
        return self._repository.add(bahan_schema=bahan_schema)
    
    def update_bahan(self, bahan_id: int, update_bahan: UpdateBahan) -> Bahan:
        return self._repository.patch(bahan_id=bahan_id, update_bahan=update_bahan)

    def delete_bahan_by_id(self, bahan_id: int) -> None:
        return self._repository.delete_by_id(bahan_id)