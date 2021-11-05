class AddressBook:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    def __str__(self):
        return "first_name: " + self.first_name + "\nlast_name: " + self.last_name + "\naddress: " + self.address \
               + "\ncity: " + self.city + "\nstate: " + self.state + "\nzip_code: " + self.zip_code + "\nphone: "\
               + self.phone + "\nemail: " + self.email

    def __dict__(self):
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
