import pytest
from address_book import Address
from address_book_main import AddressBook


@pytest.fixture()
def address_book():
    contact_1 = Address("Aashvi", "N", "Kathriguppe", "Bangalore", "Karnataka", "560064", "988212065",
                        "aashvi@gmail.com")
    address_book = AddressBook()
    address_book.add_contact(contact_1)
    return address_book


def test_adding_contact(address_book):
    assert address_book.total_count() == 1



