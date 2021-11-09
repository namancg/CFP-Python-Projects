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


def test_editing_contact(address_book):
    contact_to_update = Address("Aashvi", "Nagendra", "Kathriguppe", "Bangalore", "Karnataka", "560094", "9882120653",
                                "aashvinagendra@gmail.com")
    address_book.edit_contact(contact_to_update)
    assert address_book.total_count() == 1


def test_deleting_contact(address_book):
    person_to_be_deleted = "Aashvi"
    address_book.delete_contact(person_to_be_deleted)
    assert address_book.total_count() == 0



