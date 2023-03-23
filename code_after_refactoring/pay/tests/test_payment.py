import pytest
from pytest import MonkeyPatch
from payment import pay_order
from order import Order, LineItem

class PaymentProcessorMock:
    def charge(self, card: str, month: int, year: int, amount: int) -> None:
        print(f"Charging {card} with amount ${amount/100:.2f}")

def test_pay_order(monkeypatch: MonkeyPatch) -> None:
    inputs = ["1249190007575069", "12", "2024"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    order = Order()
    order.line_items.append(LineItem("Test", 100))
    pay_order(order, PaymentProcessorMock())
    
# This test checks for invalid orders which in this case is true because the order is empty.
def test_pay_order_invalid(monkeypatch: MonkeyPatch):
    with pytest.raises(ValueError):
        inputs = ["1249190007575069", "12", "2024"]
        monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
        order = Order()
        pay_order(order, PaymentProcessorMock())
        
    
