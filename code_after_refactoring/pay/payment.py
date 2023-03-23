from asyncio import Protocol
from order import Order

# Defining a PaymentProcessor protocol will make it much easier to introduce a mock version of this while testing
class PaymentProcessor(Protocol):
    def charge(self, card: str, month: int, year: int, amount: int) -> None:
        """Charges the card with the amount."""
    

# Refactoring this code includes adding dependency injection for the pay_order() function.
# This means providing a function in this case pay_order() with the objects that it needs.
# It will make testing easier and gives us more control over how the PaymentProcessor is created.
# It's also possible to combine dependency injection with dependency inversion then it is possible to replace the PaymentProcessor entirely without having to change anything about the pay_order() function
def pay_order(order: Order, processor: PaymentProcessor):
    if order.total == 0:
        raise ValueError("Can't pay an order with total 0.")
    card = input("Please enter your card number: ")
    month = int(input("Please enter the card expiry month: "))
    year = int(input("Please enter the card expiry year: "))
    processor.charge(card, month, year, amount=order.total)
    order.pay()