# Both LineItem and Order are imporant pieces of code to test
# This is because both of them are core data structures 
# e.g. making sure that the total actually computes the correct total amount is very important to this specific code

# LineItem class has a name, price and quantity with a property
# When testing it is important to test multiple varieties e.g. default quantity (1) and different non default quantity to see if the total is correct

# Import LineItem
from order import LineItem

# Create a test function with return value None
# This test is for the a default LineItem meaning a LineItem with default quantity 1 
def test_line_item_default() -> None:
    # Create a LineItem with name TestDefault, price 100 and no quantity meaning this is the default value of 1
    line_item = LineItem("TestDefault",100)
    # assert is used to verify if a certain value is the value that is expected
    assert line_item.total == 100 

# Create a test function with return value None
# This test is for a LineItem where the quantity is not default meaning a LineItem with quantity > 1 
def test_line_item() -> None:
    # Create a LineItem with name TestNonDefault, price 200 and quantity 5
    line_item = LineItem("TestNonDefault", 200, 5)
    assert line_item.total == 1000