from pytest import MonkeyPatch
from payment import pay_order
from order import Order, LineItem

# With monkeypatch it is possible to create mock data. 
# This needs to be done because we have input data so the test can't be run without going through this input data first
# The monkeypath.setattr allows for the overriding of the built in input system of Python -> builtins.input
# We override this with a lambda fuction that empties the inputs string sequentially meaning that each time a value is in the first element, this element wil correspond with the correct input field 
def test_pay_order(monkeypatch: MonkeyPatch) -> None:
    inputs = ["1249190007575069", "12", "2024"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    order = Order()
    order.line_items.append(LineItem("Test", 100))
    pay_order(order)
