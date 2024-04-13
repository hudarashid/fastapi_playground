from typing import Optional
from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from src.containers import Container
from .services import ProductService
from .repositories import NotFoundError
from .schemas import Product as ProductSchema

router = APIRouter()


@router.get("/products", tags=["product"])
@inject
def get_list(
        product_service: ProductService = Depends(Provide[Container.product_service]),
):
    return product_service.get_product()


@router.get("/product/{product_id}", tags=["product"])
@inject
def get_by_id(
        product_id: int,
        product_service: ProductService = Depends(Provide[Container.product_service]),
):
    try:
        return product_service.get_product_by_id(product_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/product", status_code=status.HTTP_201_CREATED, tags=["product"])
@inject
def add(
        product_schema: ProductSchema,
        product_service: ProductService = Depends(Provide[Container.product_service]),
):
    return product_service.create_product(product_schema)

@router.patch("/product/{product_id}", status_code=status.HTTP_200_OK, tags=["product"])
@inject
def patch(
        product_id: int,
        update_product: ProductSchema,
        product_service: ProductService = Depends(Provide[Container.product_service]),
):
    return product_service.update_product(product_id, update_product)


@router.delete("/product/{product_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["product"])
@inject
def remove(
        product_id: int,
        product_service: ProductService = Depends(Provide[Container.product_service]),
):
    try:
        product_service.delete_product_by_id(product_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
