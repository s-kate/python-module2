class Animal:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def display_info(self):
        print(f'Animal: {self.name}\nSpecies: {self.kind}')


class Mammal(Animal):
    def __init__(self, name, kind, nutrition):
        super().__init__(name, kind)
        self.nutrition = nutrition

    def display_info(self):
        super().display_info()
        print(f'Diet type: {self.nutrition}')


class Carnivore(Mammal):
    def __init__(self, name, kind, nutrition, number_of_teeth):
        super().__init__(name, kind, nutrition)
        self.teeth = number_of_teeth

    def display_info(self):
        super().display_info()
        print(f'Teeth Count: {self.teeth}')


class Lion(Carnivore):
    def __init__(self, name, kind, nutrition, number_of_teeth, mane_size):
        super().__init__(name, kind, nutrition, number_of_teeth)
        self.mane = mane_size

    def display_info(self):
        super().display_info()
        print(f'Mane Size: {self.mane}')


lion = Lion("Simba", "Lion", "Carnivore", 30, "Large")
carnivore = Carnivore("Tiger", "Carnivore", "Carnivore", 40)
mammal = Mammal("Elephant", "Mammal", "Herbivore")

lion.display_info()
print("-------------------------")
carnivore.display_info()
print("-------------------------")
mammal.display_info()
