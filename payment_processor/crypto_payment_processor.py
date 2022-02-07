from order.order import Order


class CryptoPaymentProcessor:

    def __init__(self, customer_email: str) -> None:
        self.__customer_email = customer_email

    def pay(self, order: Order) -> None:
        print(f"Email {self.__customer_email} validated")
        order.finish_order()
        print(f"Payment in the amout of {order.get_total_price()} processed using Ethereum")