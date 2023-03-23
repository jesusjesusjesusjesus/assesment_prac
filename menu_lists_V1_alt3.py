combos = {}
for i in range(1, 11):
    items_key = f"items_{i}"
    prices_key = f"prices_{i}"
    combos[f"cmb_{i}"] = {items_key: [None, None, None], prices_key: [None, None, None]}
