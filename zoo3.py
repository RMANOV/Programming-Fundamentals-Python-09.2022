

class Zoo:

    __animals = 0


    def __init__(self, name_of_zoo):

        self.name_of_zoo = name_of_zoo
        self.mamals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species):
        Zoo.__animals += 1

    def get_info(self, species):
        return f'{species} in {self.name_of_zoo}: {Zoo.__animals}'

    def get_total(self):
        return f'Total animals: {Zoo.__animals}'












# Path: zoo3.py