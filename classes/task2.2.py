
class Animal:
    hungry = True
    voice = ''
    def __add__(self, other):
        return self.weight + other.weight

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def speak(self):
        print(self.voice)

    def feed(self):
        self.hungry = False
        print('Животное сыто')
    def heaviest(self, *args):
        if self.weight == heavy_weight:
            print('Самое тяжелое животное: ', self.name)

class Birds(Animal):
    def __init__(self, name, weight, eggs):
        super().__init__(name, weight)
        self.eggs = eggs

    def milk(self):
        self.eggs = 0
        print('Животное подоена')


class Cattle(Animal):
    def __init__(self, name, weight, litres):
        super().__init__(name, weight)
        self.litres = litres

    def milk(self):
        self.litres = 0
        print('Животное подоена')


class Sheep(Animal):
    voice = 'Беeee'
    kg_fur = 5

    def cut(self):
        self.kg_fur = 0
        print('Овца пострижена')


class Goat(Cattle):
    voice = 'Меее'


class Duck(Birds):
    voice = 'Кря'


class Goose(Birds):
    voice = 'Га га га'

class Chicken(Birds):
    voice = 'Ко-ко'


cow = Cattle('Манька', 100, 10)
goose_1 = Goose('Серый', 8, 5)
goose_2 = Goose('Белый', 9, 4)
sheep_1 = Sheep('Барашек', 90)
sheep_2 = Sheep('Кудрявый', 80)
chicken_1 = Chicken('Ко-во', 5, 3)
chicken_2 = Chicken('Кукареку', 6, 4)
goat_1 = Goat('Рога', 35, 3)
goat_2 = Goat('Копыта', 45, 4)
duck = Duck('Кряква', 10, 2)


print('Общий вес животных состовляет: ',
      cow.weight + goose_1.weight + goose_2.weight + sheep_1.weight + sheep_2.weight +
      chicken_1.weight + chicken_2.weight + goat_1.weight + goat_2.weight + duck.weight, 'кг')

weight_animal_list = [cow.weight, goose_1.weight, goose_2.weight, sheep_1.weight, sheep_2.weight, chicken_1.weight, chicken_2.weight, goat_1.weight, goat_2.weight, duck.weight]
heavy_weight = (max(weight_animal_list))

Animal.heaviest(cow, goose_1, goose_2, sheep_1, sheep_2, chicken_1, chicken_2, goat_1, goat_2, duck)


