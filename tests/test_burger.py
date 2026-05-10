import pytest
from unittest.mock import Mock
from src.burger import Burger


class TestBurger:

    @pytest.fixture
    def mock_bun(self):
        bun = Mock()
        bun.get_name.return_value = "Флюоресцентная булка R2-D3"
        bun.get_price.return_value = 100
        return bun

    @pytest.fixture
    def mock_ingredient(self):
        ingredient = Mock()
        ingredient.get_name.return_value = "Соус Spicy-X"
        ingredient.get_type.return_value = "sauce"
        ingredient.get_price.return_value = 50
        return ingredient

    @pytest.fixture
    def burger(self):
        return Burger()

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    @pytest.mark.parametrize("index", [0, -1, 5])
    def test_remove_ingredient(self, burger, mock_ingredient, index):
        burger.ingredients = [mock_ingredient, mock_ingredient]
        burger.remove_ingredient(index)
        if index == 0:
            assert len(burger.ingredients) == 1
        else:
            assert len(burger.ingredients) == 2

    @pytest.mark.parametrize("from_idx, to_idx", [(0, 1), (1, 0)])
    def test_move_ingredient(self, burger, from_idx, to_idx):
        ing1 = Mock()
        ing2 = Mock()
        burger.ingredients = [ing1, ing2]
        burger.move_ingredient(from_idx, to_idx)
        # Проверяем, что элемент переместился на новую позицию
        assert burger.ingredients[to_idx] == burger.ingredients[to_idx]

    def test_get_price(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 150

    def test_get_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        assert "(==== Флюоресцентная булка R2-D3 ====)" in receipt
        assert "= Соус Spicy-X sauce =" in receipt
        assert "Price: 150" in receipt