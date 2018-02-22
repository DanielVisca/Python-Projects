import datetime
from UnconventionalLiving.Tax import CanadaTax
"""
Things to consider here, Full income before tax might be good to know, to calculate best places to put money,
If I assume to always contribute to TFSA first than RRSP I should state as much in the info sheet.

Amount that is wanted as an annual budget needs to be taken into consideration, I need to decide if that will be dealt
with here or elsewhere.
"""

"""
Note to self. The reason I didnt originally calculate Tax was becasue contributions to RRSP are a Tax Deduction.
I think I should calulate the tax, Find RRSP contributions than recalculate tax? Is this needless?
"""
class Savings:
    def __init__(self, income, age, province, annual_budget=30000, in_TFSA=0):
        """
        Initialize an instance of savings with different savings options

        :param income:
        :param annual_budget:
        :param in_TFSA: The amount that the user already has in their TFSA
        """
        self.age = int(age)
        self.province = province

        # Annual
        self.annual_budget = int(annual_budget)
        self.income = int(income)
        self.ct = CanadaTax()
        self.income_after_tax = self.ct.after_tax_income(self.income, self.province)

        self.amount_to_save = self.income_after_tax - self.annual_budget
        self.annual_TFSA = 0
        self.annual_RRSP = 0
        self.annual_savings = 0
        self.in_TFSA = int(in_TFSA)

        # Total at FI
        self.total_TFSA = 0
        self.total_RRSP = 0

        self.TFSA_eligible = self.TFSA_eligible()
        self.annual_savings_location()

    def annual_savings_location(self):

        if self.income > 70000:
            self.RRSP_contribution()
            # Here I have to take into consideration that RRSPs are Tax exempt Therefore my "after tax" has to be
            # recalculated. This seems circular
            # RRSP_contribution_after_tax = self.ct.after_tax_income(self.income - self.annual_RRSP, self.province)
            self.TFSA_contribution()
        else:
            self.TFSA_contribution()
            self.RRSP_contribution()
        print("TFSA: ", self.annual_TFSA)
        print("RRSP: ", self.annual_RRSP)
        print("Savings: ", self.amount_to_save)


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

        :return: NoneType
        """
        max_contribution = self.max_RRSP_contribution()

        # Note to Self: make sure that self.annual_RRSP isnt just a pointer to self.amount to save but takes on the
        #  number
        if self.amount_to_save < max_contribution:
            self.annual_RRSP = self.amount_to_save
            self.amount_to_save = 0
        else:
            self.annual_RRSP = max_contribution
            self.amount_to_save -= max_contribution

    def TFSA_contribution(self):
        """
        Return the suggested annual amount to place in a TFSA

        :return: NoneType
        """
        if self.amount_to_save <= self.TFSA_eligible:
            self.annual_TFSA = self.amount_to_save
            # this sets TFSA_eligible to be ready for next years calculations. 5500 is hardcoded based on th assumption
            # that it will always be the annual increase
            self.TFSA_eligible -= (self.amount_to_save + 5500)
            self.amount_to_save = 0

        else:
            self.annual_TFSA = self.TFSA_eligible
            self.TFSA_eligible = 5500
            self.amount_to_save -= self.TFSA_eligible

    def savings_contributions(self):
        """
        Return the suggested annual contributions to a savings account. This is taxed fully.

        :return:
        """

    # Helper Function for TFSA contributions
    def TFSA_eligible(self):
        """
        Design Note: Make sure this is only calculated for the initial year and not every year in the future.
        Based on your birthday, it calculates how much you are able to put in your TFSA as of today.

        :param age: int
        :return:
        """
        # 2009 - 2012 $5000 annual contribution
        # 2013 - 2014 $5500 annual contribution
        # 2015 $10,000 annual contribution
        # 2016 - 2018 $5500 annual contribution
        eligible = [5000, 5000, 5000, 5000, 5500, 5500, 10000, 5500, 5500]

        # Account for this calculator being used in future years
        now = datetime.datetime.now()
        curr_year = now.year
        future = curr_year - 2018
        to_extend = [5500] * future
        eligible.extend(to_extend)

        # 18 years old in 2009
        if ((curr_year - self.age) + 18) <= 2009:
            total_eligible = sum(eligible) - self.in_TFSA
        else:
            turned_18 = ((curr_year - self.age) + 18)
            years_not_eligible = turned_18 - 2009
            # -1 for index
            total_eligible = sum(eligible[years_not_eligible - 1:]) - self.in_TFSA

        return total_eligible


    # Helper Function For RRSP contributions
    def max_RRSP_contribution(self):
        """
        Return the maximum contribution to an RRSP given your Before tax income

        :param income: float
        :return: float
        """
        option1 = 0.18 * self.income
        cap_contribution = 24270

        if option1 <= cap_contribution:
            max_contribution = option1
        else:
            max_contribution = cap_contribution

        return max_contribution

    def aggregate_interst(self):
        """
        Assumption of 8% interest

        :return:
        """
