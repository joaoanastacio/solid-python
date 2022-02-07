from typing import Protocol

class PaymentAuthorizer(Protocol):

    def authorize(self, code: str) -> None:
        ...

    def is_authorized(self) -> bool:
        ...