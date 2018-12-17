class Error(Exception):
    pass

class ageError(Error):
    def __init__(self, age):
        """
        If inputed age is invalid, returns this error

        Attributes:
        age -- the inputed age of the user
        """

        self.age = age

class timeError(Error):
    def __init__(self, time):
        """
        If inputed time is invalid, returns this error

        Attributes: 
        time -- the inputed wake-up time by the user
        """

        self.time = time
