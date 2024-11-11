from core.models import Ingredient, IngredientsInRecipe, Recipe

recipes = [
    Recipe(
        recipe_name="Омлет",
        cooking_time=10,
        recipe_description="""
        Описание приготовления омлета
    """,
    ),
    Recipe(
        recipe_name="Блины молочные",
        cooking_time=25,
        recipe_description="Описание приготовления блинов",
    )
]

ingredients = [
    Ingredient(
        ingredient_name="Мука пшеничная", ingredient_description="высший сорт"
    ),
    Ingredient(ingredient_name="Соль"),
    Ingredient(ingredient_name="Сахар"),
    Ingredient(
        ingredient_name="Яйцо куриное", ingredient_description="0 категории"
    ),
    Ingredient(ingredient_name="Молоко"),
]

ingredients_to_recipes = [
    # 1 рецепт
    IngredientsInRecipe(recipe_id=1, ingredient_id=4, quantity="3 штуки"),
    IngredientsInRecipe(
        recipe_id=1, ingredient_id=2, quantity="по-вкусу"
    ),
    IngredientsInRecipe(
        recipe_id=1, ingredient_id=5, quantity="500 миллилитров"
    ),

    # 2 рецепт
    IngredientsInRecipe(
        recipe_id=2, ingredient_id=1, quantity="250 грамм"
    ),
    IngredientsInRecipe(
        recipe_id=2, ingredient_id=5, quantity="200 миллилитров"
    ),
    IngredientsInRecipe(recipe_id=2, ingredient_id=2, quantity="по-вкусу"),
    IngredientsInRecipe(recipe_id=2, ingredient_id=3, quantity="по-вкусу"),

]
