

class Zoo:

    __animals = 0


    def __init__(self, name_of_zoo):

        self.name_of_zoo = name_of_zoo
        self.mamals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):

        if species == 'mammal':

            self.mamals.append(name)
            Zoo.__animals += 1

        elif species == 'fish':

            self.fishes.append(name)
            Zoo.__animals += 1

        elif species == 'bird':

            self.birds.append(name)
            Zoo.__animals += 1

    def get_info(self, species):            
            if species == 'mammal':    
                return f'Mammals in {self.name_of_zoo}: {", ".join(self.mamals)}'    
            elif species == 'fish':    
                return f'Fishes in {self.name_of_zoo}: {", ".join(self.fishes)}'    
            elif species == 'bird':    
                return f'Birds in {self.name_of_zoo}: {", ".join(self.birds)}'

    def get_total(self):        
        return f'Total animals: {Zoo.__animals}'

zoo_name = input()
zoo = Zoo(zoo_name)

n = int(input())

for _ in range(n):    
        species, name = input().split()
        zoo.add_animal(species, name)

species = input()
print(zoo.get_info(species))
print(zoo.get_total())



















# Path: zoo3.py