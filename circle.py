

class Circle:

    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        return 2 * Circle.__pi * self.radius

    def calculate_area(self):
        return Circle.__pi * self.radius ** 2

    def calculate_area_of_sector(self, angle):
        return (angle / 360) * Circle.__pi * self.radius ** 2

        


#     def calculate_circumference(self):
#         return self.diameter * Circle.__pi

#     def calculate_area(self):
#         return (self.diameter / 2) ** 2 * Circle.__pi

#     def calculate_area_of_sector(self, angle):
#         return (angle / 360) * Circle.calculate_area(self)

# diameter = int(input())
# angle = int(input())

# circle = Circle(diameter)
# print(f'{circle.calculate_circumference():.2f}')
# print(f'{circle.calculate_area():.2f}')
# print(f'{circle.calculate_area_of_sector(angle):.2f}')

# Path: circle.py
