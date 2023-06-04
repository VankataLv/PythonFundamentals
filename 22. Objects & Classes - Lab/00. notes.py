class Person:
    def __init__(self, name, age, kg):      # <- constructor, parameters can be default (age = 0)
        self.name = name                # <- characteristics (attributes)
        self.age = age
        self.kg = kg

    def eat(self):                      # If a function is inside a class is called METHOD
        print("I am eating")
        self.kg += 0.3                  # Methods have access to the attributes of the class


test_person = Person("Test Testov", 5, 80)   # var which is a class -> self = test_person
print(test_person)                           # test_person is an instance of the class Person
print(test_person.name)
print(test_person.age)
print(test_person.kg)
test_person.eat()
print(test_person.kg)
#   _________________________________________________________________________________________


class Person:
    species = "mammal"          # <- This is a class attribute, it is for all instances the same

    def __init__(self, name, age):
        self.name = name
        self.age = age


me = Person("Peter", 25)  # me.species = "mammal"
you = Person("John", 44)  # you.species = "mammal"
