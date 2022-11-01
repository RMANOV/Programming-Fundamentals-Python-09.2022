

class Zoo:

    __animals = 0
    mamals = []
    fishes = []
    birds = []

    def __init__(self, name_of_zoo):
        self.name_of_zoo = name_of_zoo

    def add_animal(self, species):
        Zoo.__animals += 1

    def get_info(self, species):
        return f'{species} in {self.name_of_zoo}: {Zoo.__animals}'

    def get_total(self):
        return f'Total animals: {Zoo.__animals}'

    def add_mammal(self, mammal):
        Zoo.mamals.append(mammal)

    def get_mammals(self):
        











zoo_name = input()

zoo = Zoo(zoo_name)

while True:
    command = input()
    if command == 'End':
        break

    species = command
    zoo.add_animal(species)

print(zoo.get_info(species))
print(zoo.get_total())

# Path: zoo3.py