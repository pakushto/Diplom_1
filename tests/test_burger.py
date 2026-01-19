from unittest.mock import Mock
from praktikum.burger import Burger

class TestBurger:
    def test_set_buns(self):
        bun = Mock()
        burger = Burger()
        bun.get_price.return_value = 15
        burger.set_buns(bun)
        
        assert burger.bun == bun

    def test_add_ingredient(self):
        ingredient = Mock()        
        burger = Burger()

        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients

    def test_remove_ingredient(self):
        ingredient = Mock()
        burger = Burger()
        burger.ingredients = [ingredient]

        burger.remove_ingredient(0)

        assert ingredient not in burger.ingredients

    def test_move_ingredient(self):
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        burger = Burger()
        burger.ingredients = [ingredient_1, ingredient_2]
    
        burger.move_ingredient(0, 1)

        assert burger.ingredients == [ingredient_2, ingredient_1]

    def test_get_price(self):
        bun = Mock()
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        burger = Burger()
        bun.get_price.return_value = 15
        ingredient_1.get_price.return_value = 10
        ingredient_2.get_price.return_value = 5
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        total_price = burger.get_price()

        assert total_price == 45  # 15*2 + 10 + 5

    def test_get_receipt(self):
        bun = Mock()
        bun.get_name.return_value = "Булочка с кунжутом"
        bun.get_price.return_value = 15

        ingredient = Mock()
        ingredient.get_name.return_value = "Кетчуп"
        ingredient.get_type.return_value = "SAUCE"
        ingredient.get_price.return_value = 5

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        receipt = burger.get_receipt()

        expected_receipt = (
            "(==== Булочка с кунжутом ====)\n"
            "= sauce Кетчуп =\n"
            "(==== Булочка с кунжутом ====)\n\n"
            "Price: 35"
        )

        assert receipt == expected_receipt
