class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, amount):
        self.quantity = min(self.size, self.quantity + amount)

    def status(self):
        return max(0, self.size - self.quantity)
