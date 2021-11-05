from address_book import AddressBook

address_books = []

contact_1 = AddressBook("Naman", "Chandra", "Basavanagudi", "Bangalore", "Karnataka", "560004", "9538169967",
                        "naman@gmail.com")
address_books.append(contact_1)
contact_2 = AddressBook("Raksha", "R", "JP Nagar", "Bangalore", "Karnataka", "560034", "95945887845",
                        "raksha@gmail.com")
address_books.append(contact_2)
print(contact_1)
print(contact_2)


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
