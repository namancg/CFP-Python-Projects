import pytest
from address_book import Address
from address_book_main import AddressBook
import os


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


def test_search_by_city(address_book):
    city_to_be_searched = "Bangalore"
    address_book.search_contact_by_city(city_to_be_searched)
    assert address_book.total_count() == 1


def test_search_by_state(address_book):
    state_to_be_searched = "Karnataka"
    address_book.search_contact_by_state(state_to_be_searched)
    assert address_book.total_count() == 1


def test_write_and_read_to_json(address_book):
    json_file = "sample.json"
    address_book.write_to_json(json_file)
    assert os.path.isfile(json_file)
    address_book.read_from_json(json_file)
    assert address_book.total_count() == 1


def test_mapping_state_with_person(address_book):
    state_person_mapping = address_book.map_state_with_person()
    assert state_person_mapping["Karnataka"][0].first_name == "Aashvi"


def test_mapping_city_with_person(address_book):
    city_person_mapping = address_book.map_city_with_person()
    assert city_person_mapping["Bangalore"][0].first_name == "Aashvi"


# NEGATIVE TEST CASES
@pytest.mark.xfail
def test_adding_contact_with_wrong_count(address_book):
    assert address_book.total_count() == 5


@pytest.mark.xfail
def test_editing_contact_wrong_count(address_book):
    contact_to_update = Address("Aashvi", "Nagendra", "Kathriguppe", "Bangalore", "Karnataka", "560094", "9882120653",
                                "aashvinagendra@gmail.com")
    address_book.edit_contact(contact_to_update)
    assert address_book.total_count() == 8


@pytest.mark.xfail
def test_deleting_contact_wrong_count(address_book):
    person_to_be_deleted = "Aashvi"
    address_book.delete_contact(person_to_be_deleted)
    assert address_book.total_count() == 2


@pytest.mark.xfail
def test_search_by_city_wrong_count(address_book):
    city_to_be_searched = "Bangalore"
    address_book.search_contact_by_city(city_to_be_searched)
    assert address_book.total_count() == 6


@pytest.mark.xfail
def test_search_by_state_wrong_count(address_book):
    state_to_be_searched = "Karnataka"
    address_book.search_contact_by_state(state_to_be_searched)
    assert address_book.total_count() == 4


@pytest.mark.xfail
def test_write_and_read_to_json_wrong_count(address_book):
    json_file = "sample.json"
    address_book.write_to_json(json_file)
    assert os.path.isfile(json_file)
    address_book.read_from_json(json_file)
    assert address_book.total_count() == 2


@pytest.mark.xfail
def test_mapping_state_with_person_wrong_count(address_book):
    state_person_mapping = address_book.map_state_with_person()
    assert state_person_mapping["Karnataka"][0].first_name == "Aash"


@pytest.mark.xfail
def test_mapping_city_with_person_wrong_count(address_book):
    city_person_mapping = address_book.map_city_with_person()
    assert city_person_mapping["Bangalore"][0].first_name == "Aashv"
