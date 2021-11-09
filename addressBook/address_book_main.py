from address_book import Address
import json

address_books = []


class AddressBook:

    def __init__(self):
        self.address_books = []

    def add_contact(self, contact):
        """
        :param contact: the contact which is to be added
        :return: nill
        """
        self.address_books.append(contact)

    def edit_contact(contact_to_edit, updated_contact):
        """
        :param updated_contact: contact to be updated
        :return:
        """
        for i in range(len(address_books)):
            contact = address_books[i]
            if contact.phone == contact_to_edit:
                address_books[i] = updated_contact

    def __str__(self):
        """
        method to return object as string
        :return: object as a string line
        """
        string = ''
        for i in range(len(self.address_books)):
            contact = self.address_books[i]
            string += "Contact Number: {}: {}\n".format(i + 1, contact)
        return string

    def total_count(self):
        """
        :return: length of addressBook
        # """
        # length = len(address_books)
        return len(self.address_books)

    def delete_contact(self, contact_to_delete):
        """
        :param contact_to_delete: the contact which is to be deleted
        :return: nill
        """
        for i in range(len(self.address_books)):
            contact = self.address_books[i]
            if contact.first_name == contact_to_delete:
                self.address_books.remove(contact)

    def search_contact_by_city(self, city_to_search):
        """
        :param city_to_search: city to be searched
        :return: the contacts which has the given city
        """
        for i in range(len(self.address_books)):
            contact = self.address_books[i]
            if contact.city == city_to_search:
                print(contact)

    def search_contact_by_state(self, state_to_search):
        """
        :param state_to_search: the state which is to be searched
        :return: the contact which has the states present
        """
        for i in range(len(self.address_books)):
            contact = self.address_books[i]
        if contact.state == state_to_search:
            print(contact)

    def write_to_json(self, json_file):
        """
        :param json_file:the file to be written into
        :return: nill
        """
        address_books_dictionary = {"addressbooks": []}
        for i in range(len(self.address_books)):
            contact = self.address_books[i]
        address_books_dictionary["addressbooks"].append(contact.__dict__())

        with open(json_file, "w") as outfile:
            json.dump(address_books_dictionary, outfile)

    def read_from_json(self, json_file1):
        """
        :param json_file1: the file to be reading data from
        :return: the data in json file
        """
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
            address_books.append(Address(first_name, last_name, address, city, state, zip_code, phone, email))

    def map_state_with_person(self):
        """
        :return: the dictionary with person mapped with state
        """
        person_state_mapping = dict()
        for i in range(len(self.address_books)):
            contact = self.address_books[i]
            if contact.city not in person_state_mapping.keys():
                person_state_mapping[contact.city] = [contact]
            else:
                person_state_mapping[contact.city].append(contact)
        return person_state_mapping

    def map_city_with_person(self):
        """
        :return: the dictionary with person mapped with city
        """
        person_city_mapping = dict()
        for i in range(len(self.address_books)):
            contact = self.address_books[i]
            if contact.city not in person_city_mapping.keys():
                person_city_mapping[contact.city] = [contact]
            else:
                person_city_mapping[contact.city].append(contact)
        return person_city_mapping


if __name__ == "__main__":
    address_book = AddressBook()
    print(
        "1.ADD CONTACT \n2.EDIT CONTACT \n3.DELETE CONTACT \n4.WRITE TO JSON \n5.READ FROM JSON \n6.SEARCH BY CITY "
        "\n7.SEARCH BY STATE \n8.CITY PERSON MAPPING \n9.STATE PERSON MAPPING")
    print("ENTER THE OPERATION TO BE PERFORMED")
    choice = int(input())
    if choice == 1:
        contact_1 = Address("Naman", "Chandra", "Basavanagudi", "Bangalore", "Karnataka", "560004", "9538169967",
                            "naman@gmail.com")
        contact_2 = Address("Raksha", "R", "JP Nagar", "Bangalore", "Karnataka", "560034", "95945887845",
                            "raksha@gmail.com")
        contact_3 = Address("Sanjit", "Kangovi", "ISRO Layout", "Noida", "Delhi", "460034", "7259332866",
                            "sanjit@gmail.com")
        address_book.add_contact(contact_1)
        address_book.add_contact(contact_2)
        address_book.add_contact(contact_3)
        print(address_book)
    elif choice == 2:
        print("AFTER EDITING")
        contact_to_edit = "9538169967"
        updated_contact = Address("Naman", "Chandra", "Basavanagudi", "Bangalore", "Karnataka", "560004",
                                  "+919538169967",
                                  "namanchandra@gmail.com")
        address_book.edit_contact(contact_to_edit)
        print(address_book)
    elif choice == 3:
        contact_to_delete = "Sanjit"
        address_book.delete_contact(contact_to_delete)
        print("AFTER DELETING")
        print(address_book)
    elif choice == 4:
        json_file = "sample.json"
        print("WRITING TO JSON FILE")
        address_book.write_to_json(json_file)
    elif choice == 5:
        print("READING FROM JSON")
        json_file = "sample.json"
        address_book.read_from_json(json_file)
        print(address_book)
    elif choice == 6:
        city_to_search = "Bangalore"
        address_book.search_contact_by_city(city_to_search)
    elif choice == 7:
        state_to_search = "Delhi"
        address_book.search_contact_by_state(state_to_search)
    elif choice == 8:
        print("CITY PERSON MAPPING")
        city_person_mapping = address_book.map_city_with_person()
        for key, value in city_person_mapping.items():
            print("City: {}, Person Count: {}".format(key, len(value)))
            for contact in value:
                print(contact)
    elif choice == 9:
        print("STATE PERSON MAPPING")
        person_state_mapping = address_book.map_state_with_person()
        for key, value in person_state_mapping.items():
            print("State: {}, Person Count: {}".format(key, len(value)))
            for contact in value:
                print(contact)
