import re


class UserRegistration():
    def check_first_name(self, name_to_be_checked):
        pattern = "[A-Z]{1}[a-z]{1,}"
        result = re.match(pattern, name_to_be_checked)
        if result:
            print("NAME IS PROPER")
        else:
            print("ENTER VALID NAME")


if __name__ == "__main__":
    user_registration = UserRegistration()
    first_name = input("ENTER NAME TO BE CHECKED")
    user_registration.check_first_name(first_name)
