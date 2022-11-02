

class Inventory:
    __capacity = 0
    __items = []

    def __init__(self, capacity):
        self.__capacity = capacity

    def add_item(self, item):
        if self.__capacity > len(self.__items):
            self.__items.append(item)
        return f'not enough room in the inventory'

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        result = f'Items: {", ".join(self.__items)}.\nCapacity left: {self.get_capacity() - len(self.__items)}'
        return result

inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)

