from order import LineItem, Order, OrderStatus

#When testing the order class it is important to test: 
# making sure that if the LineItem is empty the total of that LineItem is 0
# making sure that if a LineItem is created the total of that LineItem is the expected total of that LineItem meaning that we don't get a total of a different LineItem

# Create a test function with return value None
# # This test is for a order where there is no LineItem present 
def test_empty_order_total() -> None:
    # Create an order without a LineItem meaning this order is empty and the total is expected to be 0 
    order = Order()
    assert order.total == 0

# Create a test function with return value None  
def test_order_total() -> None: 
    # Create an order with a LineItem that has name test, price 100 and quantity default (1) as its properties
    # the total is expected to be 100 * 1 = 100 
    order = Order()
    order.line_items.append(LineItem(name="test", price=100))
    assert order.total == 100

# Create a test function with return value None    
def test_orders_total() -> None: 
    # Create multiple orders with each a LineItem that has name test, price 100 and quantity default (1) as its properties
    # the total is expected to be (100 * 1) * 2 = 200 
    order = Order()
    order.line_items.append(LineItem(name="test", price=100))
    order.line_items.append(LineItem(name="test", price=100))
    assert order.total == 200

# Create a test function with return value None   
def test_order_pay() -> None:
    # Create an order and test the status of the order
    # when an order is paid (done with order.pay()) the status should be PAID
    order = Order()
    order.pay()
    assert order.status == OrderStatus.PAID