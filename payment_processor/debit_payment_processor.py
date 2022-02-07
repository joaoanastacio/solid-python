from order.order import Order

class DebitPaymentProcessor:

    def pay(self, order: Order, security_code: str) -> None:
        print(f"Security code {security_code} validated")
        order.finish_order()
        print(f"Debit payment in the amount of {order.get_total_price()} processed")
        