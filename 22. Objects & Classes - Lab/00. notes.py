class Person:
    def __init__(self, name, age, kg):      # <- constructor, parameters can be default (age = 0)
        self.name = name                # <- characteristics (attributes)
        self.age = age
        self.kg = kg


test_person = Person("Test Testov", 5, 80)   # var which is a class -> self = test_person
print(test_person)
print(test_person.name)
print(test_person.age)
print(test_person.kg)
#   _________________________________________________________________________________________
