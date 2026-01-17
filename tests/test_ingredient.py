import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

INGREDIENT_DATA = [
    (INGREDIENT_TYPE_SAUCE, "Кетчуп", 100),
    (INGREDIENT_TYPE_FILLING, "Котлета", 200)
]

class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_DATA)
    def test_get_name_returns_correct_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_DATA)
    def test_get_price_returns_correct_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_DATA)
    def test_get_type_returns_correct_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type