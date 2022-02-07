from decimal import InvalidOperation
from order.order import Order
from payment_authorizer.payment_authorizer import PaymentAuthorizer

class CreditPaymentProcessor:

    def __init__(self, security_code: str, authorizer: PaymentAuthorizer) -> None:
        self.__security_code = security_code
        self.__authorizer = authorizer

    def pay(self, order: Order) -> None:
        if not self.__authorizer.is_authorized():
            raise Exception("Not authorized to complete this payment")
        
        print(f"Security code {self.__security_code} validated")
        order.finish_order()
        print(f"Credit payment in the amout of {order.get_total_price()} processed")
