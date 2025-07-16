import pytest
from unittest.mock import Mock
from praktikum_code.burger import Burger


class TestBurger:

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_get_receipt(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        assert "(==== Test Bun ====)" in receipt
        assert "= sauce test ingredient =" in receipt.lower()
        assert "Price: 250.0" in receipt

    @pytest.mark.parametrize("bun_price", [50.0, 100.0, 200.5])
    def test_get_price_with_various_buns(self, bun_price, mock_ingredient):
        bun = Mock()
        bun.get_price.return_value = bun_price

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(mock_ingredient)

        expected_price = bun_price * 2 + mock_ingredient.get_price()
        assert burger.get_price() == expected_price

    @pytest.mark.parametrize("ingredient_prices", [
        [50.0],
        [20.0, 30.0],
        [10.0, 15.0, 25.0]
    ])
    def test_get_price_with_various_ingredients(self, mock_bun, ingredient_prices):
        burger = Burger()
        burger.set_buns(mock_bun)

        total_ingredients_price = 0
        for price in ingredient_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            ingredient.get_name.return_value = "X"
            ingredient.get_type.return_value = "SAUCE"
            burger.add_ingredient(ingredient)
            total_ingredients_price += price

        expected = mock_bun.get_price() * 2 + total_ingredients_price
        assert burger.get_price() == expected

    @pytest.mark.parametrize("ingredients, from_idx, to_idx, expected_order", [
        (["a", "b", "c"], 2, 0, ["c", "a", "b"]),
        (["x", "y"], 0, 1, ["y", "x"]),
    ])
    def test_move_ingredient(self, ingredients, from_idx, to_idx, expected_order, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        mocks = []
        for name in ingredients:
            ing = Mock()
            ing.get_name.return_value = name
            ing.get_type.return_value = "FILLING"
            ing.get_price.return_value = 50
            burger.add_ingredient(ing)
            mocks.append(ing)

        burger.move_ingredient(from_idx, to_idx)

        assert [i.get_name() for i in burger.ingredients] == expected_order
