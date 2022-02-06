from abc import ABC, abstractmethod

class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order, security_code):
        pass
