class Burger:
    def __init__(self):
        self.bun = None
        self.ingredients = []

    def set_buns(self, bun):
        self.bun = bun

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, index):
        if 0 <= index < len(self.ingredients):
            self.ingredients.pop(index)

    def move_ingredient(self, from_index, to_index):
        if 0 <= from_index < len(self.ingredients) and 0 <= to_index < len(self.ingredients):
            ingredient = self.ingredients.pop(from_index)
            self.ingredients.insert(to_index, ingredient)

    def get_price(self):
        price = 0
        if self.bun:
            price += self.bun.get_price()
        for ingredient in self.ingredients:
            price += ingredient.get_price()
        return price

    def get_receipt(self):
        receipt = []
        if self.bun:
            receipt.append(f"(==== {self.bun.get_name()} ====)")
        for ingredient in self.ingredients:
            receipt.append(f"= {ingredient.get_name()} {ingredient.get_type()} =")
        if self.bun:
            receipt.append(f"(==== {self.bun.get_name()} ====)")
        receipt.append(f"Price: {self.get_price()}")
        return "\n".join(receipt)