from pydantic import BaseModel, ConfigDict
from typing import List, Dict


class RecipeBase(BaseModel):
    recipe_name: str = "Блины молочные"
    cooking_time: int = 25
    views: int = 7
    recipe_description: str = "Тонкие блины на молоке. Нежные и вкусные."


class IngredientsInRecipe(BaseModel):
    ingredient_id: int
    quantity: str = "Количество продукта"


class RecipeCreate(RecipeBase):
    ingredients_in_recipe: List[IngredientsInRecipe]


class RecipeRead(RecipeBase):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id: int
