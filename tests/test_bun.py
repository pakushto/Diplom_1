import pytest
from praktikum.bun import Bun

BUN_DATA = [
    ("Булочка с кунжутом", 15),
    ("Мягкая булочка", 20),
    ("Бриошь", 300)
]

class TestBun:
    @pytest.mark.parametrize("name, price", BUN_DATA)
    def test_get_name_returns_correct_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", BUN_DATA)
    def test_get_price_returns_correct_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price