from pay.order import Order
from pay.processor import PaymentProcessor

# This is where the pay_order() function is defined.
# It gets an order as parameter
def pay_order(order: Order):
    # Check to see if the order value is above 0, this is obvious because you can't place an order if the value is 0 or below.
    if order.total == 0:
        raise ValueError("Can't pay an order with total 0.")
    # Read in some inputs from the user
    card = input("Please enter your card number: ")
    month = int(input("Please enter the card expiry month: "))
    year = int(input("Please enter the card expiry year: "))
    # Create a payment processor with an API key
    payment_processor = PaymentProcessor("6cfb67f3-6281-4031-b893-ea85db0dce20")
    # Create a charge via payment processor on the card
    payment_processor.charge(card, month, year, amount=order.total)
    # Once finished the order is set to the paid status
    order.pay()