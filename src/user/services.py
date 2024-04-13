from typing import Iterator

from .repositories import UserRepository
from .schemas import User as UserSchema
from src.user.models import User


class UserService:

    def __init__(self, user_repository: UserRepository) -> None:
        self._repository: UserRepository = user_repository

    def get_users(self) -> Iterator[User]:
        return self._repository.get_all()

    def get_user_by_id(self, user_id: int) -> User:
        return self._repository.get_by_id(user_id)

    def create_user(self, user_schema: UserSchema) -> User:
        return self._repository.add(user_schema=user_schema)

    def delete_user_by_id(self, user_id: int) -> None:
        return self._repository.delete_by_id(user_id)