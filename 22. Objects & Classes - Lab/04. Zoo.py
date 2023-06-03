class Zoo:
    __animals = 0           # <- __ means that it is a private attribute not meant to be used outside the class

    def __init__(self, name_zoo):
        self.name_zoo = name_zoo
        self.mammals = list()
        self.fishes = list()
        self.birds = list()

    def add_animal(self, species, name_animal):
        if species == "mammal":
            self.mammals.append(name_animal)
        elif species == "fish":
            self.fishes.append(name_animal)
        elif species == "bird":
            self.birds.append(name_animal)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            animals_present = f"Mammals in {self.name_zoo}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            animals_present = f"Fishes in {self.name_zoo}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            animals_present = f"Birds in {self.name_zoo}: {', '.join(self.birds)}\n"

        animals_present += f"Total animals: {Zoo.__animals}"
        return animals_present

zoo = Zoo(input())
an_count = int(input())
for i in range(an_count):
    command = input()
    spec, nam = command.split(" ")
    zoo.add_animal(spec, nam)
print(zoo.get_info(input()))
