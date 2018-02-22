def toFI(income, years=1,TFSA=0, RRSP=0, savings=0):
    """
    Errors: only federal tax currently calculated in
    :param income:
    :param TFSA:
    :param RRSP:
    :param savings:
    :param years:
    :return:
    """
    OGincome = income
    TFSAcanContribute = 55000 - TFSA
    RRSPcanContribute = income * 0.18
    annualSpending = 0
    yearCanFI = None
    previousTFSAcontribution = 0
    previousRRSPcontribution = 0
    previousAfterTaxcontribution = 0


    #Repeat for every year saved
    for i in range(years):

        income = OGincome
        taxable = 30000
        income -= 30000

        #calculate interest from last year and add to appropriate places. Comment out if savings not self invested
        TFSA += previousTFSAcontribution * 0.08
        savings += previousAfterTaxcontribution * 0.08
        RRSP += previousRRSPcontribution * 0.08

        if i != 0:
            TFSAcanContribute += 5500 #subject to change

        if OGincome <= 30000:
            print(0)
            return 0
        else:

            #contribute max to TFSA
            if (TFSAcanContribute > 0):
                if income > TFSAcanContribute:
                    TFSA += TFSAcanContribute
                    income -= TFSAcanContribute
                    previousTFSAcontribution = TFSAcanContribute
                    TFSAcanContribute = 0


                else:
                    TFSA += income
                    previousTFSAcontribution = income
                    TFSAcanContribute -= income
                    income = 0

            #contribute as much as you can to RRSP
            if income != 0:
                if income > RRSPcanContribute:
                    RRSP += RRSPcanContribute
                    income -= RRSPcanContribute
                    previousRRSPcontribution = RRSPcanContribute

                else:
                    RRSP += income
                    previousRRSPcontribution = income
                    income = 0

            #possible issue: if it is taxable I already added it to savings so it has to come out of spending
            if income != 0:
                taxable += income
                income = 0
            #calculate tax
            aftertax = calculateAfterFedTax(taxable)

            if aftertax <= 30000:
                annualSpending = aftertax

            if aftertax > 30000:
                aftertax -= 30000
                annualSpending = 30000
                previousAfterTaxcontribution = aftertax
                savings += aftertax


            annualSpending = round(annualSpending,2)
            totalSaved = round(TFSA + RRSP + savings,2)
            savings = round(savings,2)
            monthly = round(annualSpending/12,2)
#make this work for multiple years of saving

            if checkIfFI(totalSaved) and yearCanFI == None:
                yearCanFI = i + 1
    print(" income: $" + str(OGincome) + "\n annual budget: $" + str(annualSpending) + " \n monthly budget: $" + str(
        monthly) + "\n total saved: $" + str(totalSaved) + "\n TFSA: $" + str(TFSA) + "\n RRSP: $" + str(
        RRSP) + "\n savings: $" + str(savings) + "\n can retire after " + str(yearCanFI) + " years of working \n \n")


    blogTincome = (OGincome + 15000)
    flipTincome = int(OGincome + 10000)
    vendingTincome = int(OGincome + 6000)
    allThree = int(OGincome + 31000)

    print(" if you owned 3 average vending machines you could ")
    FIonlyCalculator(vendingTincome,years,0,0,0)
    print(" if you flipped products online for profit you could ")
    FIonlyCalculator(flipTincome, years,0,0,0)
    print(" if you added a blog as a side hussel you could ")
    FIonlyCalculator(blogTincome,years,0,0,0)
    print(" if you flipped items online, owned 3 vending machines and ran a blog you could ")
    FIonlyCalculator(allThree,years,0,0,0)


    return (" income: $" + str(OGincome) + "\n annual budget: $" +str(
        annualSpending) + " \n monthly budget: $" + str(monthly) + "\n total saved: $" + str(
        totalSaved) + "\n TFSA: $" + str(TFSA) + "\n RRSP: $" + str(RRSP) + "\n savings: $" + str(savings))

def calculateAfterFedTax(taxable,lowestBracket=45282,lowBracPercent=0.85,secondBracket=90563,secondPercent=0.795,thirdBracket=140388,thirdPercent=0.74,forthBracket=200000,forthPercent=0.67):
    #add in the '<=' stuff also I am doing one calculation too many on each one
    #lowest Bracket
    if taxable <= lowestBracket:
        aftertax = taxable * lowBracPercent
        return aftertax

    #second Bracket
    elif lowestBracket < taxable < secondBracket:

        #first
        aftertax = lowestBracket * lowBracPercent
        taxable -= lowestBracket

        #second
        aftertax += taxable * secondPercent
        return round(aftertax,2)

    #third Bracket
    elif secondBracket < taxable < thirdBracket:
        #first
        aftertax = lowestBracket * lowBracPercent
        taxable -= lowestBracket

        #second
        aftertax += (secondBracket - lowestBracket) * secondPercent
        taxable -= (secondBracket - lowestBracket)

        #third
        aftertax += taxable * thirdPercent
        return round(aftertax,2)

    #forth Bracket
    elif thirdBracket < taxable < forthBracket:
        # first
        aftertax = lowestBracket * lowBracPercent
        taxable -= lowestBracket

        # second
        aftertax += (secondBracket - lowestBracket) * secondPercent
        taxable -= (secondBracket - lowestBracket)

        # third
        aftertax += (thirdBracket - secondBracket) * thirdPercent
        taxable -= (thirdBracket - secondBracket)

        #forth
        aftertax += taxable * forthPercent
        return round(aftertax,2)

    elif forthBracket < taxable:
        # first
        aftertax = lowestBracket * lowBracPercent
        taxable -= lowestBracket

        # second
        aftertax += (secondBracket - lowestBracket) * secondPercent
        taxable -= (secondBracket - lowestBracket)

        # third
        aftertax += (thirdBracket - secondBracket) * thirdPercent
        taxable -= (thirdBracket - secondBracket)

        #forth
        aftertax += (forthBracket - thirdBracket) * forthPercent
        taxable -= (forthBracket - thirdBracket)

        #last
        aftertax += taxable * forthPercent
        return round(aftertax, 2)

def checkIfFI(saved):
    if saved > 1000000:
        return True
    else:
        return False

#Recommended side income: Ebooks/author, vending machines, flipping things online, run a blog, run a website with ad revenue, ecomerce store
#ebook on kindle selling for $2.99 makes $4500 a year. Shown from this website http://upfuel.com/how-much-money-can-one-kindle-book-make-1-year-case-study/
#Also the books rank was 22,160 with a high point of 11,000.
#make $2.09 for every $2.99 sale

#vending $3000 a machine a year as rev. or $2000 profit?
#super conservative 10k to 15k flipping items online
#blogging 15k - 20k (could be way way more ?
def FIonlyCalculator(income, years=1,TFSA=0, RRSP=0, savings=0, firstTime=True):
    OGincome = income
    TFSAcanContribute = 55000 - TFSA
    RRSPcanContribute = income * 0.18
    annualSpending = 0
    yearCanFI = None
    previousTFSAcontribution = 0
    previousRRSPcontribution = 0
    previousAfterTaxcontribution = 0

    # Repeat for every year saved
    for i in range(years):

        income = OGincome
        taxable = 30000
        income -= 30000

        # calculate interest from last year and add to appropriate places. Comment out if savings not self invested
        TFSA += previousTFSAcontribution * 0.08
        savings += previousAfterTaxcontribution * 0.08
        RRSP += previousRRSPcontribution * 0.08

        if i != 0:
            TFSAcanContribute += 5500  # subject to change

        if OGincome <= 30000:
            print(0)
            return 0
        else:

            # contribute max to TFSA
            if (TFSAcanContribute > 0):
                if income > TFSAcanContribute:
                    TFSA += TFSAcanContribute
                    #I think this income is still taxed
                    #income -= TFSAcanContribute
                    previousTFSAcontribution = TFSAcanContribute
                    TFSAcanContribute = 0


                else:
                    TFSA += income
                    previousTFSAcontribution = income
                    TFSAcanContribute -= income
                    income = 0

            # contribute as much as you can to RRSP
            if income != 0:
                if income > RRSPcanContribute:
                    RRSP += RRSPcanContribute
                    income -= RRSPcanContribute
                    previousRRSPcontribution = RRSPcanContribute

                else:
                    RRSP += income
                    previousRRSPcontribution = income
                    income = 0

            # possible issue: if it is taxable I already added it to savings so it has to come out of spending
            if income != 0:
                taxable += income
                income = 0
            # calculate tax
            aftertax = calculateAfterFedTax(taxable)

            if aftertax <= 30000:
                annualSpending = aftertax

            if aftertax > 30000:
                aftertax -= 30000
                annualSpending = 30000
                previousAfterTaxcontribution = aftertax
                savings += aftertax

            annualSpending = round(annualSpending, 2)
            totalSaved = round(TFSA + RRSP + savings, 2)
            savings = round(savings, 2)
            monthly = round(annualSpending / 12, 2)
            # make this work for multiple years of saving

            if checkIfFI(totalSaved) and yearCanFI == None:
                yearCanFI = i + 1
    print (" retire after " + str(yearCanFI) + " years of working \n")
    return yearCanFI

#savings(150000,10)
toFI(60000,40)