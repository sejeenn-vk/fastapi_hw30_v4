from pydantic import BaseModel, ConfigDict


class RecipeBase(BaseModel):
    recipe_name: str
    cooking_time: int
    views: int
    recipe_description: str


class RecipeCreate(RecipeBase):
    ...


class RecipeRead(RecipeBase):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id: int
