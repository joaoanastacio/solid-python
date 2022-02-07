from order.order import Order
from payment_authorizer.payment_authorizer import PaymentAuthorizer

class CryptoPaymentProcessor:

    def __init__(self, customer_email: str, authorizer: PaymentAuthorizer) -> None:
        self.__customer_email = customer_email
        self.__authorizer = authorizer

    def pay(self, order: Order) -> None:
        if not self.__authorizer.is_authorized():
            raise Exception("Not authorized to complete this payment")
            
        print(f"Email {self.__customer_email} validated")
        order.finish_order()
        print(f"Payment in the amout of {order.get_total_price()} processed using Ethereum")
        