class ShoppingCart:
    def __init__(self):
        self.cart = {}  

    def add_item(self, item, quantity=1):
        if item in self.cart:
            self.cart[item] += quantity
        else:
            self.cart[item] = quantity
        print(f"Added {quantity} {item}(s) to the cart.")

    def remove_item(self, item, quantity=1):
        if item in self.cart:
            if self.cart[item] <= quantity:
                del self.cart[item]
                print(f"Removed {item} from the cart.")
            else:
                self.cart[item] -= quantity
                print(f"Removed {quantity} {item}(s) from the cart.")
        else:
            print(f"{item} not found in the cart.")

    def view_cart(self):
        if self.cart:
            print("Items in the cart:")
            for item, quantity in self.cart.items():
                print(f"{item}: {quantity}")
        else:
            print("The cart is empty.")

cart = ShoppingCart()
cart.add_item("Laptop", 1)
cart.add_item("Mouse", 2)
cart.view_cart()

cart.remove_item("Mouse")
cart.view_cart()

cart.remove_item("Laptop", 1)
cart.view_cart()

cart.remove_item("Keyboard")  
