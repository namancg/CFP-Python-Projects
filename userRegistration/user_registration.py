import re


class UserRegistration():
    def check_name(self, first_name, last_name):
        """
        :param first_name: first name input to be checked
        :param last_name: last name input to be checked
        :return: if the entered name is proper or not
        """
        pattern = "[A-Z]{1}[a-z]{1,}"
        result = re.match(pattern, first_name)
        if result:
            print("NAME IS PROPER")
        else:
            print("ENTER VALID FIRST NAME")

        result = re.match(pattern, last_name)
        if result:
            print("NAME IS PROPER")
        else:
            print("ENTER VALID LAST NAME")

    def check_email(self, email_to_be_checked):
        """
        :param email_to_be_checked: email-id to be checked
        :return: if the email-id is proper or not
        """
        pattern = "^[a-zA-z]+[a-zA-Z0-9]*[- . + _]?[a-zA-Z0-9]+[@]{1}[a-z0-9]+[.]{1}[a-z]+[.]?[a-z]+$"
        result = re.match(pattern, email_to_be_checked)
        if result:
            print("EMAIL ID IS PROPER")
        else:
            print("ENTER VALID EMAIL ID")

    def check_mobile_number(self, mobile_number_to_be_checked):
        pattern = "(0|91)?[0-9][0-9]{9}"
        result = re.match(pattern, mobile_number_to_be_checked)
        if result:
            print("MOBILE NUMBER IS PROPER")
        else:
            print("ENTER VALID MOBILE NUMBER")

    def check_password(self, password_to_be_checked):
        pattern = "[a-zA-Z0-9].{8,}"
        result = re.match(pattern, password_to_be_checked)
        if result:
            print("PASSWORD IS PROPER")
        else:
            print("ENTER VALID PASSWORD")


if __name__ == "__main__":
    user_registration = UserRegistration()
    first_name = input("ENTER FIRST NAME TO BE CHECKED")
    last_name = input("ENTER LAST NAME TO BE CHECKED")
    user_registration.check_name(first_name, last_name)

    email_id = input("ENTER THE EMAIL TO BE CHECKED")
    user_registration.check_email(email_id)

    phone_number = input("ENTER MOBILE NUMBER")
    user_registration.check_mobile_number(phone_number)

    password = input("ENTER PASSWORD")
    user_registration.check_password(password)
