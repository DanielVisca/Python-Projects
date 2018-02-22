from UnconventionalLiving.Tax import CanadaTax
from UnconventionalLiving.Savings import Savings

if __name__ == "__main__":

    canada_tax = CanadaTax()
    income = input("Annual Income: ")
    province = input("Province: ")
    after_tax = canada_tax.after_tax_income(income, province)
    print (after_tax)
    age = input("Your age: ")
    in_TFSA = input("Amount currently in your TFSA: ")
    annual_budget = input("Desired annual Budget: ")
    savings = Savings(income, age, province, annual_budget, in_TFSA)
    print(savings.TFSA_eligible)