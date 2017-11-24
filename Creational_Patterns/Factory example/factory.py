""""Author: Hernández Venegas José Zenaido
    gmail: josehdz3321@gmail.com
    date: 11/11/2017
    Description: Creacion de una clase donde
    los objetos comparten atributos parecidos."""


class Dog:
    """"A single dog class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"


class Cat:
    """"A single dog class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"


def get_pet(pet="dog"):
    """"The factory method"""
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]


d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())
