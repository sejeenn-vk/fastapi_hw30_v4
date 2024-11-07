from typing import Annotated, List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Ingredient
from core.schemas.ingredient import IngredientRead, IngredientCreate
from api.crud import ingredient as ingredient_crud

ingredient_route = APIRouter()


@ingredient_route.get(
    "/ingredients", tags=["Вывести список ингредиентов"],
    response_model=List[IngredientRead]
)
async def get_all_ingredients(
        session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
        ],
):
    ingredients = await ingredient_crud.get_all_ingredients(session=session)
    return ingredients


@ingredient_route.post(
    "/ingredients",
    tags=["Добавить новый ингредиент"],
    response_model=IngredientRead,
)
async def add_new_ingredient(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        ingredient_data: IngredientCreate,
):
    ingredient = await ingredient_crud.create_ingredient(
        session=session,
        ingredient_create=ingredient_data,
    )
    return ingredient
