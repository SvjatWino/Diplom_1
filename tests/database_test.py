import pytest
from praktikum_code.database import Database
from praktikum_code.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum_code.bun import Bun
from praktikum_code.ingredient import Ingredient


class TestDatabase:

    def test_available_buns_returns_correct_buns(self):
        db = Database()
        buns = db.available_buns()

        assert isinstance(buns, list)
        assert all(isinstance(b, Bun) for b in buns)
        assert len(buns) == 3
        names = [bun.get_name() for bun in buns]
        assert "black bun" in names
        assert "white bun" in names
        assert "red bun" in names

    def test_available_ingredients_returns_correct_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()

        assert isinstance(ingredients, list)
        assert all(isinstance(i, Ingredient) for i in ingredients)
        assert len(ingredients) == 6

        sauces = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]

        assert len(sauces) == 3
        assert len(fillings) == 3

        sauce_names = [i.get_name() for i in sauces]
        filling_names = [i.get_name() for i in fillings]

        assert "hot sauce" in sauce_names
        assert "sour cream" in sauce_names
        assert "chili sauce" in sauce_names

        assert "cutlet" in filling_names
        assert "dinosaur" in filling_names
        assert "sausage" in filling_names
