class UserRegistrationException(Exception):
    """
    THIS IS USED WHEN INPUT VALUE IS NONE OR EMPTY
    """
    def __init__(self, message):
        self.message = message

