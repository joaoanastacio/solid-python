from order.order import Order
from order.order_item import OrderItem
from payment_processor.crypto_payment_processor import CryptoPaymentProcessor
from payment_authorizer.facebook_payment_authorizer import FacebookPaymentAuthorizer

def main() -> None:

    order = Order()
    first_item = OrderItem("MacBook Pro", 2, 2500.00)
    second_item = OrderItem("MacBook Air", 2, 1500.00)

    order.add_item(first_item)
    order.add_item(second_item)
    print(order.get_total_price())

    payment_authorizer = FacebookPaymentAuthorizer()
    payment_authorizer.authorize("ZXT54300HK")
    payment_processor = CryptoPaymentProcessor("profissional.anastacio@gmail.com", payment_authorizer)
    payment_processor.pay(order)

if __name__ == "__main__":
    main()
