from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Ingredient
from core.schemas.ingredient import IngredientCreate

#
# async def get_all_users(
#         session: AsyncSession,
# ) -> Sequence[User]:
#     stmt = select(User).order_by(User.id)
#     result = await session.scalars(stmt)
#     return result.all()


async def create_ingredient(
        session: AsyncSession,
        ingredient_create: IngredientCreate,
) -> Ingredient:
    ingredient = Ingredient(**ingredient_create.model_dump())
    session.add(ingredient)
    await session.commit()
    # await session.refresh(user)
    return ingredient
