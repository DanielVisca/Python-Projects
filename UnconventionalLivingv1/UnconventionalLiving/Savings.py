"""
Things to consider here, Full income before tax might be good to know, to calculate best places to put money,
If I assume to always contribute to TFSA first than RRSP I should state as much in the info sheet.

Amount that is wanted as an annual budget needs to be taken into consideration, I need to decide if that will be dealt
with here or elsewhere.
"""
class Savings:
    def __init__(self, after_tax_income):
        """
        Initialize an instance of savings with different savings options
        """
        self.income = after_tax_income

    def total_contributions_for_FI(self):
        """
        Return the total amount in each account that will be accumulated after the number of years to hit FI

        :return:
        """
    # Consider if this function should be located in this class or not
    def years_to_FI(self):
        """
        Return the number of years of working until FI is reached
        :return:
        """

    def RRSP_contribution(self):
        """
        Return the suggested annual amount to place in an RRSP

        :return: float
        """

    def TFSA_contributions(self):
        """
        Return the suggested annual amount to place in a TFSA

        :return: float
        """

    def savings_contributions(self):
        """
        Return the suggested annual contributions to a savings account. This is taxed fully.

        :return:
        """

    # Helper Function for TFSA contributions
    def TFSA_eligable(age):
        """
        Based on your birthday, it calculates how much you are able to put in your TFSA as of today.

        :param age: int
        :return:
        """

    # Helper Function For RRSP contributions
    def max_RRSP_contribution(income):
        """
        Return the maximum contribution to an RRSP given your Before tax income

        :param income: float
        :return: float
        """
        # Currently 18% of income can be added
        return income * 0.18