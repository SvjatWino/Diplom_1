import pytest
from unittest.mock import Mock


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "Test Bun"
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.get_name.return_value = "Test Ingredient"
    ingredient.get_type.return_value = "SAUCE"
    ingredient.get_price.return_value = 50.0
    return ingredient

