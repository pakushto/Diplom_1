import pytest
from praktikum.bun import Bun

BUN_NAMES = [
    "Булочка с кунжутом",
    "brioche-XL",
    "bun_with_underscores_123",
    "!@#-special-name",
]

BUN_PRICES = [0, 1.5, 300, 9999]


class TestBun:
    @pytest.mark.parametrize("name", BUN_NAMES)
    def test_get_name_returns_correct_name(self, name):
        bun = Bun(name, price=42)

        assert bun.get_name() == name

    @pytest.mark.parametrize("price", BUN_PRICES)
    def test_get_price_returns_correct_price(self, price):
        bun = Bun(name="Фиксированное имя", price=price)

        assert bun.get_price() == price
