num_cars = int(input())
inventory = {}
for i in range(num_cars):
    car, mileage, fuel = input().split("|")
    mileage = int(mileage)
    fuel = int(fuel)
    inventory[car] = [mileage, fuel]  # 0->mileage , 1-> fuel
command = input()
while command != "Stop":
    action, details = command.split(" : ", 1)
    if action == "Drive":
        car, distance, fuel_needed = details.split(" : ")
        distance = int(distance)
        fuel_needed = int(fuel_needed)
        if fuel_needed > inventory[car][1]:
            print("Not enough fuel to make that ride")
        else:
            inventory[car][0] += distance
            inventory[car][1] -= fuel_needed
            print(f"{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
            if inventory[car][0] >= 100000:
                print(f"Time to sell the {car}!")
                inventory.pop(car)
    elif action == "Refuel":
        car, fuel_add = details.split(" : ")
        fuel_add = int(fuel_add)
        fuel_to_be_added = 75 - inventory[car][1]
        if fuel_to_be_added >= fuel_add:
            print(f"{car} refueled with {fuel_add} liters")
            inventory[car][1] += fuel_add
        else:
            print(f"{car} refueled with {fuel_to_be_added} liters")
            inventory[car][1] += fuel_to_be_added
    elif action == "Revert":
        car, kms = details.split(" : ")
        kms = int(kms)
        inventory[car][0] -= kms
        if inventory[car][0] < 10000:
            inventory[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kms} kilometers")
    command = input()
for key, value in inventory.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")
