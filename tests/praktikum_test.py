from unittest.mock import patch, MagicMock
import pytest
import praktikum_code.praktikum as praktikum


@patch("praktikum_code.praktikum.Database")
@patch("praktikum_code.praktikum.Burger")
def test_main_workflow(mock_burger_cls, mock_database_cls):
    # Моки базы данных
    mock_database = MagicMock()
    mock_buns = [MagicMock()]
    mock_ingredients = [MagicMock() for _ in range(6)]
    mock_database.available_buns.return_value = mock_buns
    mock_database.available_ingredients.return_value = mock_ingredients
    mock_database_cls.return_value = mock_database

    # Мок бургера
    mock_burger = MagicMock()
    mock_burger_cls.return_value = mock_burger

    # Вызываем main
    praktikum.main()

    # Проверки вызовов
    mock_database_cls.assert_called_once()
    mock_database.available_buns.assert_called_once()
    mock_database.available_ingredients.assert_called_once()

    mock_burger_cls.assert_called_once()
    mock_burger.set_buns.assert_called_once_with(mock_buns[0])

    assert mock_burger.add_ingredient.call_count == 4
    mock_burger.add_ingredient.assert_any_call(mock_ingredients[1])
    mock_burger.add_ingredient.assert_any_call(mock_ingredients[4])
    mock_burger.add_ingredient.assert_any_call(mock_ingredients[3])
    mock_burger.add_ingredient.assert_any_call(mock_ingredients[5])

    mock_burger.move_ingredient.assert_called_once_with(2, 1)
    mock_burger.remove_ingredient.assert_called_once_with(3)
    mock_burger.get_receipt.assert_called_once()
