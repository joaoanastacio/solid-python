from payment_processor import PaymentProcessor
from order.order import Order
from typing import Type

class CreditPaymentProcessor(PaymentProcessor):

    def pay(self, order: Type[Order], security_code: str):
        pass