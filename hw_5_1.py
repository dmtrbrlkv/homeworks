import time
class Person():
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.__know = []

    def know(self, person):
        if person not in self.__know:
            self.__know.append(person)
            person.know(self)

    def is_know(self, person):
        if person in self.__know:
            return self.name + " знаком с " + person.name
        else:
            return self.name + " не знаком с " + person.name


petya = Person(18, "Петя")
vasya = Person(21, "Вася")
olya = Person(16, "Оля")


petya.know(olya)
vasya.know(olya)

print(olya.is_know(petya))
print(petya.is_know(vasya))
