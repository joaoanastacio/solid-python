from tkinter.messagebox import NO


class OrderItem:

    def __init__(self, name, quantity, price) -> None:
        self.name = name
        self.__quantity = quantity
        self.__price = price

    def get_price(self) -> float:
        return self.__quantity * self.__price

    def increase_quantity(self) -> None:
        self.__quantity = self.__quantity + 1

    def decrease_quantity(self) -> None:
        self.__quantity = self.__quantity - 1
