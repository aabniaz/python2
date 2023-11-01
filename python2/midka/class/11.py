class Menu:
    def __init__(self):
        self.menu_items = {}

    def add_item(self, item_name, price):
        self.menu_items[item_name] = price
        print(f"Added {item_name} to the menu for ${price}.")

    def remove_item(self, item_name):
        if item_name in self.menu_items:
            del self.menu_items[item_name]
            print(f"Removed {item_name} from the menu.")
        else:
            print(f"{item_name} is not in the menu.")

    def display_menu(self):
        if self.menu_items:
            print("Menu:")
            for item, price in self.menu_items.items():
                print(f"{item}: ${price}")
        else:
            print("The menu is empty.")

class Restaurant:
    def __init__(self):
        self.menu = Menu()
        self.orders = []

    def take_order(self, item_name):
        if item_name in self.menu.menu_items:
            self.orders.append(item_name)
            print(f"Added {item_name} to the order.")
        else:
            print(f"Sorry, {item_name} is not available in the menu.")

    def display_orders(self):
        if self.orders:
            print("Current Orders:")
            for order in self.orders:
                print(order)
        else:
            print("No orders placed yet.")

restaurant = Restaurant()
restaurant.menu.add_item("Burger", 10)
restaurant.menu.add_item("Pizza", 15)
restaurant.menu.display_menu()

restaurant.take_order("Burger")
restaurant.take_order("Pizza")
restaurant.take_order("Pasta") 
restaurant.display_orders()
