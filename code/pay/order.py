from dataclasses import dataclass, field
from enum import Enum

# the order has two statuses it can either be open or it can be paid
# by default each order is set to open
class OrderStatus(Enum):
    OPEN = "open"
    PAID = "paid"


# each LineItem has a name, price and quantity
# if the quantity is not set it will receive 1 as its default value
@dataclass
class LineItem:
    name: str
    price: int
    quantity: int = 1

    # compute the price for each LineItem
    @property
    def total(self) -> int:
        return self.price * self.quantity


@dataclass
class Order:
    line_items: list[LineItem] = field(default_factory=list)
    status: OrderStatus = OrderStatus.OPEN

    # compute the price for each order (totals of every LineItem)
    @property
    def total(self) -> int:
        return sum(item.total for item in self.line_items)

    # Setting order status from open to paid
    def pay(self) -> None:
        self.status = OrderStatus.PAID