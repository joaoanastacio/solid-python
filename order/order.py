from order.order_item import OrderItem
from typing import Type

class Order:

    def __init__(self) -> None:
        self.price = 0.0
        self.items = []
        self.status = "OPEN"

    def add_item(self, item: Type[OrderItem]) -> None:
        self.items.append(item)

    def get_total_price(self) -> float:
        total_price = 0.0

        for item in self.items:
            total_price += item.get_price()
        
        return total_price

    def finish_order(self) -> None:
        self.status = "CLOSED"