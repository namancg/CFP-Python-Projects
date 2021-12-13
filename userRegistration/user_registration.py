import re
from user_registration_exception import UserRegistrationException


class UserRegistration():
    def __init__(self):
        pass

    @staticmethod
    def check_first_name(first_name):
        """
        :param first_name: first name input to be checked
        :return: true or exception message
        """
        try:
            pattern = "[A-Z]{1}[a-z]{1,}"
            if first_name is None:
                raise UserRegistrationException("INVALID INPUT")
            if first_name == "":
                raise UserRegistrationException("EMPTY")
            result = re.match(pattern, first_name)
            if result:
                print("NAME IS PROPER")
                return True
            else:
                raise UserRegistrationException("ENTER PROPER NAME")
        except UserRegistrationException as e:
            print(e)

    @staticmethod
    def check_last_name(last_name):
        """
        :param last_name: last name input to be checked
        :return: true or exception message
        """
        try:
            pattern = "[A-Z]{1}[a-z]{1,}"
            if last_name is None:
                raise UserRegistrationException("INVALID INPUT")
            if last_name == "":
                raise UserRegistrationException("EMPTY")
            result = re.match(pattern, last_name)
            if result:
                print("NAME IS PROPER")
                return True
            else:
                raise UserRegistrationException("ENTER PROPER NAME")
        except UserRegistrationException as e:
            print(e)

    @staticmethod
    def check_email(email_to_be_checked):
        """
        :param email_to_be_checked: email-id to be checked
        :return: true or exception message
        """
        try:
            pattern = "^[a-zA-z]+[a-zA-Z0-9]*[- . + _]?[a-zA-Z0-9]+[@]{1}[a-z0-9]+[.]{1}[a-z]+[.]?[a-z]+$"
            if email_to_be_checked is None:
                raise UserRegistrationException("INVALID INPUT")
            if email_to_be_checked == "":
                raise UserRegistrationException("EMPTY")
            result = re.match(pattern, email_to_be_checked)
            if result:
                print("EMAIL ID IS PROPER")
                return True
            else:
                print("ENTER PROPER EMAIL")
                return False
        except UserRegistrationException as e:
            print(e)

    @staticmethod
    def check_mobile_number(mobile_number_to_be_checked):
        """
        :param mobile_number_to_be_checked: mobile number to be checked
        :return: true or exception message
        """
        try:
            pattern = "(0|91)?[0-9][0-9]{9}"
            if mobile_number_to_be_checked is None:
                raise UserRegistrationException("INVALID INPUT")
            if mobile_number_to_be_checked == "":
                raise UserRegistrationException("EMPTY")
            result = re.match(pattern, mobile_number_to_be_checked)
            if result:
                print("MOBILE NUMBER IS PROPER")
                return True
            else:
                raise UserRegistrationException("ENTER PROPER PHONE")
        except UserRegistrationException as e:
            print(e)

    @staticmethod
    def check_password(password_to_be_checked):
        """
        :param password_to_be_checked:password to be checked
        :return: true or exception message
        """
        try:
            pattern = "^(?=.*[a-zA-Z])([a-zA-Z]*[@#$%^&-+=()])*(?=.*[0-9]).{8,}$"
            if password_to_be_checked is None:
                raise UserRegistrationException("INVALID INPUT")
            if password_to_be_checked == "":
                raise UserRegistrationException("EMPTY")
            result = re.match(pattern, password_to_be_checked)
            if result:
                print("PASSWORD IS PROPER")
                return True
            else:
                raise UserRegistrationException("ENTER PROPER PASSWORD")
        except UserRegistrationException as e:
            print(e)


if __name__ == "__main__":
    user_registration = UserRegistration()
    first_name = input("ENTER FIRST NAME TO BE CHECKED")
    last_name = input("ENTER LAST NAME TO BE CHECKED")
    user_registration.check_first_name(first_name)
    user_registration.check_first_name(last_name)

    phone_number = input("ENTER MOBILE NUMBER")
    user_registration.check_mobile_number(phone_number)

    password = input("ENTER PASSWORD")
    user_registration.check_password(password)
