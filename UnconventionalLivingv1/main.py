def savings(income, years=1,TFSA=0, RRSP=0, savings=0):
    """
    Errors: currently TFSA and RRSP  and income work great but savings is messed up.
    :param income:
    :param TFSA:
    :param RRSP:
    :param savings:
    :param years:
    :return:
    """
    TFSAcanContribute = 55000 - TFSA
    RRSPcanContribute = income * 0.18
    annualSpending = 0
    taxable = 30000
    income -= 30000
    for i in range(years):
        if income <= 30000:
            print(0)
            return 0
        else:

            #contribute max to TFSA
            if (TFSAcanContribute > 0):
                if income > TFSAcanContribute:
                    TFSA += TFSAcanContribute
                    income -= TFSAcanContribute
                else:
                    TFSA += income
                    income = 0
            #contribute as much as you can to RRSP
            if income != 0:
                if income > RRSPcanContribute:
                    RRSP += RRSPcanContribute
                    income -= RRSPcanContribute
                else:
                    RRSP += income
                    income = 0
            #possible issue: if it is taxable I already added it to savings so it has to come out of spending
            if income != 0:
                taxable += income
                income = 0
            #calculate tax

            if taxable <= 45282:
                aftertax = taxable * 0.85
            if 45282 < taxable < 90563:
                aftertax = 45282 * 0.85
                taxable -= 45282
                aftertax += taxable * 0.795
            if 90563 < taxable < 140388 :
                aftertax = 45282 * 0.85
                taxable -= 45282
                aftertax += taxable * 0.795
                taxable -= 45281 # 90563 - 45282
                aftertax += taxable * 0.74
            if 140388 < taxable < 200000 :
                aftertax = 45282 * 0.85
                taxable -= 45282
                aftertax += taxable * 0.795
                taxable -= 45281 # 90563 - 45282
                aftertax += taxable * 0.74
                taxable -= 49825 # 140,388 - 90,563
                aftertax += taxable * 0.71
            if 200000 < taxable :
                aftertax = 45282 * 0.85
                taxable -= 45282
                aftertax += taxable * 0.795
                taxable -= 45281 # 90563 - 45282
                aftertax += taxable * 0.74
                taxable -= 49825 # 140,388 - 90,563
                aftertax += taxable * 0.71
                taxable -= 59612 # 200,000 - 140388
                aftertax += taxable * 0.67
            if aftertax > 30000:
                aftertax -= 30000
                annualSpending = 30000
                savings += aftertax
            if aftertax <= 30000:
                annualSpending = aftertax

            print("annual budget: $" +str(annualSpending) + " \n monthly budget: $" + str(annualSpending/12) + "\n total saved: $" + str(TFSA + RRSP + savings) + "\n TFSA: $" + str(TFSA) + "\n RRSP: $" + str(RRSP) + "\n savings: $" + str(savings))
            return ("annual budget: $" +str(annualSpending) + " \n monthly budget: $" + str(annualSpending/12) + "\n total saved: $" + str(TFSA + RRSP + savings) + "\n TFSA: $" + str(TFSA) + "\n RRSP: $" + str(RRSP) + "\n savings: $" + str(savings))

savings(150000, 10)