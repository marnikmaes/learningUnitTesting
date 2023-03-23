import pytest
from pytest import MonkeyPatch
from processor import PaymentProcessor
from payment import pay_order
from order import Order, LineItem

# With monkeypatch it is possible to create mock data. 
# This needs to be done because we have input data so the test can't be run without going through this input data first
# The monkeypath.setattr allows for the overriding of the built in input system of Python -> builtins.input
# We override this with a lambda fuction that empties the inputs string sequentially meaning that each time a value is in the first element, this element wil correspond with the correct input field 
# When running a test we don't actually want to pay an order with a credit card. To solve this issue the pay_order also needs to be patched and mocked
# Instead of checking the API KEY a lambda fuction is created that returns true meaning the return of the check_api_key() function will also always be true in testing.
# mocking the charge() function is also important as to not accidentally charge a card when running tests.
# We create a mock function charge_mock() and pass in the same parameters the real method has but instead of charging the card we just pass through this function

def test_pay_order(monkeypatch: MonkeyPatch) -> None:
    def charge_mock(self, card: str, month: int, year: int, amount: int) -> None:
        pass
    inputs = ["1249190007575069", "12", "2024"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    monkeypatch.setattr(PaymentProcessor, "_check_api_key", lambda _: True)
    monkeypatch.setattr(PaymentProcessor, "charge", charge_mock)
    order = Order()
    order.line_items.append(LineItem("Test", 100))
    pay_order(order)
    
# This test checks for invalid orders which in this case is true because the order is empty.
def test_pay_order_invalid(monkeypatch: MonkeyPatch):
    with pytest.raises(ValueError):
        inputs = ["1249190007575069", "12", "2024"]
        monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
        monkeypatch.setattr(PaymentProcessor, "_check_api_key", lambda _: True)
        order = Order()
        pay_order(order)
        
    
