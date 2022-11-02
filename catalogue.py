

class Catalogue:

    products = []

    def __init__(self, name):
        self.name = name

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        result = [p for p in self.products if p.startswith(first_letter)]
        return result

    def __repr__(self):
        result = ""
        result += f"Items in the {self.name} catalogue:\n"
        result += '\n'.join(sorted(self.products))
        return result
        # result = f'Items in the {self.name} catalog:\n'
        # result += '\n'.join(sorted(self.products))
        # return result
