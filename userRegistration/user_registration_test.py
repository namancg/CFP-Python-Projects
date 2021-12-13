import pytest
from user_registration import UserRegistration

user_registration = UserRegistration()
list_of_emails = [("abc@yahoo.com", True), ("abc-100@yahoo.com", True), ("abc.100@yahoo.com", True),
                  ("abc111@abc.com", True), ("abc-100@abc.net", True), ("abc.100@abc.com.au", True),
                  ("abc@1.com", True),
                  ("abc@gmail.com.com", True), ("abc+100@gmail.com", True), (".abc@abc.com", False),
                  ("abc@123@gmaila", False),
                  ("abc@abc@gmailcom", False),
                  ("abc123@gmaila", False), ("abc..2002@gmail.com", False), ("abc@abc@gmail.com", False),
                  ("abc()*@gmail.com", False), ("abc@%*@gmail.com", False),
                  ("abc@gmail.com.1a", False), ("abc@gmail.com.aa.au", False)]


@pytest.mark.parametrize("email,outcome", list_of_emails)
def test_email(email, outcome):
    assert user_registration.check_email(email) == outcome


def test_first_name():
    assert user_registration.check_first_name("Naman") == True
    assert not user_registration.check_first_name("naman")


def test_last_name():
    assert user_registration.check_last_name("Chandra") == True
    assert not user_registration.check_last_name("chandra")


def test_mobile_number():
    assert user_registration.check_mobile_number("9538169967") == True
    assert not user_registration.check_mobile_number("958 84 84")


def test_password():
    assert user_registration.check_password("Namancg@2020") == True
    assert not user_registration.check_password("nama")


# NEGATIVE TEST CASES
@pytest.mark.xfail
def test_email_wrong_outcome(email, outcome):
    assert user_registration.check_email(email) == outcome


@pytest.mark.xfail
def test_first_name_wrong_input_pattern():
    assert user_registration.check_first_name("Naman") == False
    assert not user_registration.check_first_name("naman")


@pytest.mark.xfail
def test_last_name_wrong_input_pattern():
    assert user_registration.check_last_name("Chandra") == False
    assert not user_registration.check_last_name("chandra")


@pytest.mark.xfail
def test_mobile_number_wrong_input_pattern():
    assert user_registration.check_mobile_number("9538169967") == False
    assert not user_registration.check_mobile_number("958 84 84")


@pytest.mark.xfail
def test_password_wrong_input_pattern():
    assert user_registration.check_password("Namancg@2020") == False
    assert not user_registration.check_password("nama")
