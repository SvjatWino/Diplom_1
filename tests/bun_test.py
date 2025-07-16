from praktikum_code.bun import Bun


class TestBun:

    def test_get_name_returns_correct_name(self):
        bun = Bun(name="Black Bun", price=100.0)
        assert bun.get_name() == "Black Bun"

    def test_get_price_returns_correct_price(self):
        bun = Bun(name="White Bun", price=75.5)
        assert bun.get_price() == 75.5
