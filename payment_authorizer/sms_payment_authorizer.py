class SmsPaymentAuthorizer:

    def __init__(self) -> None:
        self.__authorized = False

    def authorize(self, code: str) -> None:
        print(f"Verifying SMS code: {code}")
        self.__authorized = True

    def is_authorized(self) -> bool:
        return self.__authorized
