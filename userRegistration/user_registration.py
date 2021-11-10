import re


class UserRegistration():
    def check_name(self, first_name,last_name):
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


if __name__ == "__main__":
    user_registration = UserRegistration()
    first_name = input("ENTER FIRST NAME TO BE CHECKED")
    last_name = input("ENTER LAST NAME TO BE CHECKED")
    user_registration.check_name(first_name,last_name)
