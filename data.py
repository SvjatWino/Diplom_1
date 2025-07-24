bun_prices = [50.0, 100.0, 200.5]

ingredient_price_sets = [
    [50.0],
    [20.0, 30.0],
    [10.0, 15.0, 25.0]
]

ingredient_reorder_cases = [
    (["a", "b", "c"], 2, 0, ["c", "a", "b"]),
    (["x", "y"], 0, 1, ["y", "x"]),
]

expected_receipt = (
    "(==== Test Bun ====)\n"
    "= sauce Test Ingredient =\n"
    "(==== Test Bun ====)\n"
    "\n"
    "Price: 250.0"
)
