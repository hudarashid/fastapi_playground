from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from src.containers import Container
from .services import UserService
from .schemas import User as UserSchema
from .repositories import NotFoundError

router = APIRouter()


@router.get("/users", tags=["users"])
@inject
def get_list(
        user_service: UserService = Depends(Provide[Container.user_service]),
):
    return user_service.get_users()


@router.get("/user/{user_id}", tags=["users"])
@inject
def get_by_id(
        user_id: int,
        user_service: UserService = Depends(Provide[Container.user_service]),
):
    try:
        return user_service.get_user_by_id(user_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/user", status_code=status.HTTP_201_CREATED, tags=["users"])
@inject
def add(
        user_schema: UserSchema,
        user_service: UserService = Depends(Provide[Container.user_service]),
):
    return user_service.create_user(user_schema)


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
@inject
def remove(
        user_id: int,
        user_service: UserService = Depends(Provide[Container.user_service]),
):
    try:
        user_service.delete_user_by_id(user_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/status")
def get_status():
    return {"status": "OK"}