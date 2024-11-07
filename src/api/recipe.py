from typing import List, Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.schemas.recipe import RecipeRead, RecipeCreate
from api.crud import recipe as recipe_crud


recipe_route = APIRouter()


@recipe_route.get("/recipes", tags=["Список рецептов"], response_model=List[RecipeRead])
async def get_all_recipes(
        session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
        ],
):
    ingredients = await recipe_crud.get_all_recipes(session=session)
    return ingredients


@recipe_route.post("/recipes", tags=["Записать новый рецепт"], response_model=RecipeRead)
async def add_new_recipe(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter),],
        recipe_data: RecipeCreate,
):
    recipe = await recipe_crud.create_recipe(
        session=session,
        recipe_create=recipe_data,
    )
    return recipe
