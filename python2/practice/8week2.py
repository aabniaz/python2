class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, kolichestvo):
        if kolichestvo == 10:
            return self.price * 0.9
        elif 10 < kolichestvo < 99:
            return self.price * 0.8
        else:
            return self.price

    def make_purchase(self, kol_pokupki):
        price = self.get_price(kol_pokupki)
        if kol_pokupki <= self.amount:
            self.amount = self.amount - kol_pokupki
            return kol_pokupki, price
        else:
            return 0, 0

def check_products(products, quantities):
    available = {}
    total_cost = 0
    for product, quantity in zip(products, quantities):
        purchased, cost = product.make_purchase(quantity)
        available[product.name] = product.amount
        if purchased > 0:
            print(f'{product.name} {purchased}, Price: ${cost:.2f}')
            total_cost += cost

    print(f"Total Cost: ${total_cost:.2f}")

    return available

alma = Product('alma', 100, 10.0)
orange = Product('orange', 500, 5.0)

products = [alma, orange]
quantities = [15, 60]

remaining_products = check_products(products, quantities)
print("Remaining products: ")
for product, quantity in remaining_products.items():
    print(f'{product} {quantity}')
