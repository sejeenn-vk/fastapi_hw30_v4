from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Recipe, IngredientsInRecipe
from core.schemas.recipe import RecipeCreate


async def get_all_recipes(
        session: AsyncSession,
) -> Sequence[Recipe]:
    stmt = select(Recipe).order_by(Recipe.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_recipe(
        session: AsyncSession,
        recipe_create: RecipeCreate,
) -> Recipe:
    data = recipe_create.model_dump()
    print(data)
    recipe = Recipe(
        recipe_name=data['recipe_name'],
        cooking_time=data['cooking_time'],
        views=data['views'],
        recipe_description=data['recipe_description'],
    )
    session.add(recipe)
    await session.flush()
    ingredients_in_recipe = []
    for item in data['ingredients_in_recipe']:
        ingredients_in_recipe.append(
            IngredientsInRecipe(
                recipe_id=recipe.id,
                ingredient_id=item['ingredient_id'],
                quantity=item['quantity'],
            )
        )
    session.add_all(ingredients_in_recipe)
    await session.commit()
    return recipe
