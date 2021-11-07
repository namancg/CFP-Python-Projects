class AddressBook:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        """

        :param first_name: to store first name of the person
        :param last_name:to store last name of the person
        :param address:to store address of the person
        :param city:to store city of the person
        :param state:to store state of the person
        :param zip_code:to store zipcode of the person
        :param phone:to store phone of the person
        :param email:to store email of the person
        """
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    def __str__(self):
        """

        :return: the string to display all objects
        """
        return "first_name: " + self.first_name + "\nlast_name: " + self.last_name + "\naddress: " + self.address \
               + "\ncity: " + self.city + "\nstate: " + self.state + "\nzip_code: " + self.zip_code + "\nphone: " \
               + self.phone + "\nemail: " + self.email

    def __dict__(self):
        """

        :return:dictonary data
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "phone": self.phone,
            "email": self.email
        }
