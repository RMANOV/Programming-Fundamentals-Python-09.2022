

class Catalogue:

    products = []

    def __init__(self, name):
        self.name = name

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        result = [p for p in self.products if p[0] == first_letter]
        result.sort(Ascending=True)
        return result

    def __repr__(self):
        result = f'Items in the {self.name} catalog:\n'
        result += '\n'.join(sorted(self.products))
        return result
