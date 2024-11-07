from pydantic import BaseModel, ConfigDict


class IngredientBase(BaseModel):
    ingredient_name: str
    ingredient_description: str | None


class IngredientCreate(IngredientBase):
    pass


class IngredientRead(IngredientBase):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id: int
