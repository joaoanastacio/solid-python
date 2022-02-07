from order.order import Order

class CreditPaymentProcessor:

    def pay(self, order: Order, security_code: str) -> None:
        print(f"Security code {security_code} validated")
        order.finish_order()
        print(f"Credit payment in the amout of {order.get_total_price()} processed")
