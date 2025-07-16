from praktikum_code.ingredient import Ingredient

class TestIngredient:
    def test_get_price(self):
        ingredient = Ingredient("SAUCE", "Ketchup", 15.5)
        assert ingredient.get_price() == 15.5

    def test_get_name(self):
        ingredient = Ingredient("FILLING", "Beef", 50.0)
        assert ingredient.get_name() == "Beef"

    def test_get_type(self):
        ingredient = Ingredient("SAUCE", "Mustard", 10.0)
        assert ingredient.get_type() == "SAUCE"
