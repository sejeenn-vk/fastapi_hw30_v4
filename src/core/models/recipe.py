from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text, String
from .base import Base
from .ingredient import Ingredient
from .mixins.int_id_pk import IntIdPkMixin


class Recipe(IntIdPkMixin, Base):
    """
    Класс, описывающий рецепты
    """

    id: Mapped[int] = mapped_column(primary_key=True)
    recipe_name: Mapped[str] = mapped_column(String(100))
    cooking_time: Mapped[int] = mapped_column(default=5)
    views: Mapped[int] = mapped_column(default=0)
    recipe_description: Mapped[str] = mapped_column(
        Text, default="Здесь могла бы быть ваша реклама."
    )

    used_ingredients: Mapped[List[Ingredient]] = relationship(
        back_populates="used_in_recipe", secondary="ingredients_in_recipe"
    )

    def __repr__(self):
        return f"Recipe(id={self.id}, name={self.recipe_name})"
