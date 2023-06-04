class Vehicle:
    owner = None

    def __init__(self, type: str, model: str, price: int):
        self.type = type
        self.model = model
        self.price = price

    def buy(self, money: int, buyer: str):
        if money >= self.price and self.owner is None:
            self.owner = buyer
            return f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"
        elif money < self.price:
            return "Sorry, not enough money"
        elif self.owner is not None:
            return "Car already sold"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
