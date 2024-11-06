from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from .base import Base
from .recipe import Recipe
from .mixins.int_id_pk import IntIdPkMixin


class Ingredient(IntIdPkMixin, Base):
    """
    Класс, описывающий ингредиенты, входящие в рецепт
    """

    id: Mapped[int] = mapped_column(primary_key=True)
    ingredient_name: Mapped[str] = mapped_column(String(100))
    ingredient_description: Mapped[str | None]

    used_in_recipe: Mapped[List[Recipe]] = relationship(
        back_populates="used_ingredients", secondary="ingredients_in_recipe"
    )

    def __repr__(self):
        return f"Recipe(id={self.id}, name={self.ingredient_name})"
