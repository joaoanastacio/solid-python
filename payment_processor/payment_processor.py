from typing import Protocol

from order.order import Order

class PaymentProcessor(Protocol):

    def pay(self, order: Order, security_code: str) -> None:
        ...
