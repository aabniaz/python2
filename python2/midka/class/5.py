class Vehicle:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def __str__(self):
        return f"{self.year} {self.make} {self.model}, Mileage: {self.mileage}"

class Inventory:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Added {vehicle.year} {vehicle.make} {vehicle.model} to the inventory.")

    def remove_vehicle(self, vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)
            print(f"Removed {vehicle.year} {vehicle.make} {vehicle.model} from the inventory.")
        else:
            print("Vehicle not found in the inventory.")

    def display_inventory(self):
        if self.vehicles:
            print("Vehicles in the inventory:")
            for vehicle in self.vehicles:
                print(vehicle)
        else:
            print("The inventory is empty.")

vehicle1 = Vehicle("Toyota", "Camry", 2020, 25000)
vehicle2 = Vehicle("Honda", "Civic", 2018, 35000)

inventory = Inventory()
inventory.add_vehicle(vehicle1)
inventory.add_vehicle(vehicle2)
inventory.display_inventory()

inventory.remove_vehicle(vehicle1)
inventory.display_inventory()

inventory.remove_vehicle(vehicle1)  