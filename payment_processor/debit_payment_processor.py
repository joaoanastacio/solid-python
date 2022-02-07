from order.order import Order

class DebitPaymentProcessor:

    def __init__(self, security_code: str) -> None:
        self.__security_code = security_code

    def pay(self, order: Order) -> None:
        print(f"Security code {self.__security_code} validated")
        order.finish_order()
        print(f"Debit payment in the amount of {order.get_total_price()} processed")
        