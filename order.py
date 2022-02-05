class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "OPEN"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def get_total_price(self):
        total_price = 0

        for index in range(len(self.prices)):
            total_price += self.quantities[index] * self.prices[index]
        
        return total_price