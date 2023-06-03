class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.d = diameter

    def calculate_circumference(self):
        result = 2 * Circle.__pi * (self.d/2)
        return result

    def calculate_area(self):
        result = Circle.__pi * ((self.d/2) ** 2)
        return result

    def calculate_area_of_sector(self, angle):
        result = (angle/360) * Circle.__pi * (self.d/2) * (self.d/2)
        return result


# circle = Circle(10)
# print(f"{circle.calculate_area():.2f}")
# print(f"{circle.calculate_circumference():.2f}")
# print(f"{circle.calculate_area_of_sector(5):.2f}")
