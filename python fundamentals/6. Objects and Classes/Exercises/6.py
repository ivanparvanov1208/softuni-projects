class Inventory:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.items = []  # Instance attribute

    def add_item(self, item: str):
        if len(self.items) < self.__capacity:  # Check against the length of items
            self.items.append(item)
        else:
            return "Not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity - len(self.items)  # Return remaining capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.get_capacity()}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)

