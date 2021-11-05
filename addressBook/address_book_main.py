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
