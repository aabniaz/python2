class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, quantity):
        if quantity < 10:
            return quantity * self.price
        elif 10 <= quantity < 100:
            return quantity * self.price * 0.9  # 10% discount for quantities between 10 and 99
        else:
            return quantity * self.price * 0.8  # 20% discount for quantities of 100 or more

    def make_purchase(self, quantity):
        if quantity <= self.amount:
            self.amount -= quantity
            return f"Purchase successful! {quantity} {self.name}(s) have been bought."
        else:
            return f"Insufficient stock. We only have {self.amount} {self.name}(s) available."

product = Product("Widget", 50, 10)  # Product: Widget, Amount: 50, Price: $10 each

print(product.get_price(5))   # Output: 50 (5 items * $10 each)
print(product.get_price(15))  # Output: 135 (15 items * $9 each after 10% discount)
print(product.get_price(120)) # Output: 960 (120 items * $8 each after 20% discount)

print(product.make_purchase(10))    # Output: Purchase successful! 10 Widget(s) have been bought.
print(product.make_purchase(60))    # Output: Purchase successful! 60 Widget(s) have been bought.
print(product.make_purchase(100))   # Output: Insufficient stock. We only have 30 Widget(s) available.
