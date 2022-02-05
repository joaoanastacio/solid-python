from order_item import OrderItem

class Order:

    def __init__(self):
        self.price = 0
        self.items: OrderItem = []
        self.status = "OPEN"

    def add_item(self, item: OrderItem):
        self.items.append(item)

    def get_total_price(self):
        total_price = 0

        for item in self.items:
            total_price += item.get_price()
        
        return total_price

    def finish_order(self):
        self.status = "CLOSED"