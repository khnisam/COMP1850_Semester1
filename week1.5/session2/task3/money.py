# Week 1.5, Session 2: Task 3

class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.
        """

        if not isinstance(pounds, (int)):
            raise TypeError ("Pounds must be a number.")
        else:
            if (pounds < 0):
                print("Pounds must be a number greater than 0. ")
            else:
                self.pounds = pounds

        if not isinstance(pence, int):
            raise TypeError ("Pence must be a number.")
        else:
            if (pence < 0):
                print("Pence must be a number greater than 0. ")
            elif (pence > 99):
                print("Pence must be a number less than 99. ")
            else:
                self.pence = pence

        # Add validation code here, to check that
        # - the pounds parameter is an integer
        # - pounds is not negative
        # - the pence parameter is an integer
        # - pence is not negative and not greater than 99
        # Raise appropriate exceptions if any of these are violated

    def __str__(self):
        """
        Returns a string representation of this Money.
        """
        # Add code here to return an appropriate string representation
        # Use the currency symbol for British Pounds Sterling
        # Represent pence with a leading zero if needed (e.g. '05')

    def __add__(self, other):
        """
        Adds this Money to another Money, returning the total.
        """
        # Add code here to check that parameter 'other' is a Money object,
        # add self to other, then return the sum as a new Money object
        # (see README for hints and tips)

m = Money(-1, 5)
print(m.pounds)
print(m.pence)