from UnconventionalLiving.Tax import CanadaTax
from UnconventionalLiving.Savings import Savings
from flask import Flask, render_template
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#   return render_template('template.html')
#
# @app.route('/my-link/')
# def my_link():
#   print 'I got clicked!'
#
#   return 'Click.'
#
# if __name__ == '__main__':
#   app.run(debug=True)
if __name__ == "__main__":

    canada_tax = CanadaTax()
    income = input("Annual Income: ")
    province = input("Province: ")
    after_tax = canada_tax.after_tax_income(income, province)
    # print (after_tax)
    age = input("Your age: ")
    in_TFSA = input("Amount currently in your TFSA: ")
    annual_budget = input("Desired annual Budget: ")
    self_employed= input("Are you self_employed: ")
    savings = Savings(income, age, province, self_employed, annual_budget, in_TFSA)
    # print(savings.TFSA_eligible)