from typing import Optional
from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from src.containers import Container
from .services import BahanService
from .repositories import NotFoundError
from .schemas import Bahan as BahanSchema, UpdateBahan

router = APIRouter()


@router.get("/bahan")
@inject
def get_list(
        bahan_service: BahanService = Depends(Provide[Container.bahan_service]),
):
    return bahan_service.get_bahan()


@router.get("/bahan/{bahan_id}")
@inject
def get_by_id(
        bahan_id: int,
        bahan_service: BahanService = Depends(Provide[Container.bahan_service]),
):
    try:
        return bahan_service.get_bahan_by_id(bahan_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/bahan", status_code=status.HTTP_201_CREATED)
@inject
def add(
        bahan_schema: BahanSchema,
        bahan_service: BahanService = Depends(Provide[Container.bahan_service]),
):
    return bahan_service.create_bahan(bahan_schema)

@router.patch("/bahan/{bahan_id}", status_code=status.HTTP_200_OK)
@inject
def patch(
        bahan_id: int,
        update_bahan: UpdateBahan,
        bahan_service: BahanService = Depends(Provide[Container.bahan_service]),
):
    return bahan_service.update_bahan(bahan_id, update_bahan)


@router.delete("/bahan/{bahan_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def remove(
        bahan_id: int,
        bahan_service: BahanService = Depends(Provide[Container.bahan_service]),
):
    try:
        bahan_service.delete_bahan_by_id(bahan_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
