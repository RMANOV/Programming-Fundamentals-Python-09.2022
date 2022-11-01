

class Storage:

    storage = []

    def __init__(self, capacity):
        self.capacity = capacity

    def add_product(self, product):
        if len(Storage.storage) < self.capacity:
            Storage.storage.append(product)
        else:
            print('Error')

    def get_products(self):
        return Storage.storage

    def __repr__(self):
        return f'{Storage.storage}'
