from processor import PaymentProcessor
import pytest

# For testing purposes the API KEY is placed in this test file.
# Normally this is never done but this makes learning and practicing unit testing easier
API_KEY = "6cfb67f3-6281-4031-b893-ea85db0dce20"

# Create a test function with return value None
def test_api_key_invalid() -> None:
    # Using the with statement it is possible to declaire what type or error we are expecting.
    # In this situation if the API KEY is invalid we are expecting to get a ValueError.
    with pytest.raises(ValueError):
        # Create a processor with an emty API KEY string meaning this API KEY will be invalid
        processor = PaymentProcessor("")
        processor.charge("1249190007575069", 12, 2024, 100)

# Create a test function with return value None 
def test_card_valid_date() -> None:
    # Create a processor with valid API KEY and valid parameters
    processor = PaymentProcessor(API_KEY)
    processor.charge("1249190007575069", 12, 2024, 100)

# Create a test function with return value None   
def test_card_invalid_date() -> None:
    with pytest.raises(ValueError):
        # Create a processor with valid API KEY but invalid date parameters
        processor = PaymentProcessor(API_KEY)
        processor.charge("1249190007575069", 12, 1900, 100)

# Right now the luhn_checksum() tests are being run in this file but in truth these are seperate from the payment processor.
# Better is to seperate these from the payment processor object to make the tests simpler
# But for practice I keep these here for now

def test_card_number_invalid_luhn():
    # Create a processor with valid API KEY but invalid card number according to the luhn_checksum()
    payment_processor = PaymentProcessor(API_KEY)
    assert not payment_processor.luhn_checksum("1249190007575068")

def test_card_number_valid_luhn():
    # Create a processor with valid API KEY and valid card number according to the luhn_checksum()
    payment_processor = PaymentProcessor(API_KEY)
    assert payment_processor.luhn_checksum("1249190007575069")
    
def test_charge_card_valid():
    # Create a processor with valid API KEY and valid charge parameters
    payment_processor = PaymentProcessor(API_KEY)
    payment_processor.charge("1249190007575069", 12, 2024, 100)
    
def test_charge_card_invalid():
    # Create a processor with valid API KEY but invalid charge parameters to make sure this raises a ValueError
    with pytest.raises(ValueError):
        payment_processor = PaymentProcessor(API_KEY)
        payment_processor.charge("1249190007575068", 12, 2024, 100)