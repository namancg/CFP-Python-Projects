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


# FUNCTION TO EDIT CONTACT
def edit_contact(contact_to_edit, updated_contact):
    for i in range(len(address_books)):
        contact = address_books[i]
        if contact.phone == contact_to_edit:
            address_books[i] = updated_contact


contact_to_edit = "9538169967"
updated_contact = AddressBook("Naman", "Chandra", "Basavanagudi", "Bangalore", "Karnataka", "560004", "+919538169967",
                              "namanchandra@gmail.com")
edit_contact(contact_to_edit, updated_contact)


# FUNCTION TO PRINT ADDRESSBOOK
def print_addressBook():
    for i in range(len(address_books)):
        contact = address_books[i]
        print(contact)


print("AFTER UPDATING")
print_addressBook()


# FUNCTION TO DELETE CONTACT
def delete_contact(contact_to_delete):
    for i in range(len(address_books)):
        contact = address_books[i]
        if contact.first_name == contact_to_delete:
            address_books.remove(contact)


contact_to_delete = "Raksha"
delete_contact(contact_to_delete)
print("AFTER DELETING")
print_addressBook()


# FUNCTION TO SEARCH CONTACT BY CITY
def search_contact_by_city(city_to_search):
    for i in range(len(address_books)):
        contact = address_books[i]
        if contact.city == city_to_search:
            print(contact)


city_to_search = "Bangalore"
search_contact_by_city(city_to_search)


# FUNCTION TO SEARCH CONTACT BY STATE
def search_contact_by_state(state_to_search):
    for i in range(len(address_books)):
        contact = address_books[i]
        if contact.state == state_to_search:
            print(contact)


state_to_search = "Delhi"
search_contact_by_state(state_to_search)


# FUNCTION TO WRITE TO JSON
def write_to_json(json_file):
    address_books_dictionary = {"addressbooks": []}
    for i in range(len(address_books)):
        contact = address_books[i]
        address_books_dictionary["addressbooks"].append(contact.__dict__())
    with open(json_file, "w") as outfile:
        json.dump(address_books_dictionary, outfile)


json_file = "sample.json"
print("WRITING TO JSON FILE")
write_to_json(json_file)


# FUNCTION TO READ FROM JSON
def read_from_json(json_file1):
    global address_books
    address_books = []
    with open(json_file1) as infile:
        data = json.load(infile)
    for contact in data["addressbooks"]:
        first_name = contact["first_name"]
        last_name = contact["last_name"]
        address = contact["address"]
        city = contact["city"]
        state = contact["state"]
        zip_code = contact["zip_code"]
        phone = contact["phone"]
        email = contact["email"]
        address_books.append(AddressBook(first_name, last_name, address, city, state, zip_code, phone, email))


print("READING FROM JSON")
read_from_json(json_file)
