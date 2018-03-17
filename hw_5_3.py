class Animal():
    def __init__(self, name, animal_type):
        self.name = name
        if isinstance(animal_type, list):
            self.animal_type = animal_type
        else:
            self.animal_type = [animal_type]


class Human():
    dangerous_types = ("хищник", "ядовитый")

    def is_dangerous(self, animal):
        animal_type = animal.animal_type
        for a_type in animal_type:
            if a_type.lower() in self.dangerous_types:
                return True
        return False


snake = Animal("Змея", ["Ядовитый", "Хищник"])
cow = Animal("Корова", "Травоядный")
bear = Animal("Медведь", "Хищник")

man = Human()

print(man.is_dangerous(snake))
print(man.is_dangerous(cow))
print(man.is_dangerous(bear))
