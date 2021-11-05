from address_book import AddressBook
import json

address_books = []

contact_1 = AddressBook("Naman", "Chandra", "Basavanagudi", "Bangalore", "Karnataka", "560004", "9538169967",
                        "naman@gmail.com")
address_books.append(contact_1)
contact_2 = AddressBook("Raksha", "R", "JP Nagar", "Bangalore", "Karnataka", "560034", "95945887845",
                        "raksha@gmail.com")
address_books.append(contact_2)
contact_3 = AddressBook("Sanjit", "Kangovi", "ISRO Layout", "Noida", "Delhi", "460034", "7259332866",
                        "sanjit@gmail.com")
address_books.append(contact_3)
print(contact_1)
print(contact_2)
print(contact_3)


def edit_contact(contact_to_edit, updated_contact):
    for i in range(len(address_books)):
        contact = address_books[i]
        if contact.phone == contact_to_edit:
            address_books[i] = updated_contact


contact_to_edit = "9538169967"
updated_contact = AddressBook("Naman", "Chandra", "Basavanagudi", "Bangalore", "Karnataka", "560004", "+919538169967",
                              "namanchandra@gmail.com")
edit_contact(contact_to_edit, updated_contact)


def print_addressBook():
    for i in range(len(address_books)):
        contact = address_books[i]
        print(contact)


print("AFTER UPDATING")
print_addressBook()


def delete_contact(contact_to_delete):
    for i in range(len(address_books)):
        contact = address_books[i]
        if contact.first_name == contact_to_delete:
            address_books.remove(contact)


contact_to_delete = "Raksha"
delete_contact(contact_to_delete)
print("AFTER DELETING")
print_addressBook()


def search_contact_by_city(city_to_search):
    for i in range(len(address_books)):
        contact = address_books[i]
        if contact.city == city_to_search:
            print(contact)


address_books.append(contact_2)
city_to_search = "Bangalore"
search_contact_by_city(city_to_search)


def search_contact_by_state(state_to_search):
    for i in range(len(address_books)):
        contact = address_books[i]
        if contact.state == state_to_search:
            print(contact)


state_to_search = "Delhi"
search_contact_by_state(state_to_search)
