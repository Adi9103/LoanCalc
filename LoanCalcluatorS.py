import math

def intCheck(interest):
    if interest <= 0:
        print("Incorrect parameters.")
        exit()

def princCheck(principal):
    if principal <=0:
        print("Incorrect parameters.")
        exit()

def periodCheck(periods):
    if periods <=0:
        print("Incorrect parameters.")
        exit()

def payCheck(payment):
    if payment <=0:
        print("Incorrect parameters.")
        exit()


print("What do you want to calculate?\n")
print('Annuity Payment: Type "annuity"')
print('Differentiated Payment: Type "diff')
paymentType = str(input())

if paymentType == "annuity":
    print('Number of Monthly Payments: Type "n"')
    print('Monthly Payment Amount: Type "m"')
    print('Loan Principal: Type "p"\n')
    resultType = str(input())



    if resultType == "m":



        principal = int(input("Enter the loan principal: "))
        princCheck(principal)

        payment = int(input("Enter monthly payment: "))
        payCheck(payment)

        interest = float(input("Enter the loan interest: "))
        intCheck(interest)


        interest = (interest) / (12*100)
        inLog = payment / (payment - interest*principal)
        periods = math.log(inLog, 1+interest)
        periodsCopy = periods
        if periods%1>=0:
            periods = math.ceil(periods)
        numYear = periods//12
        if numYear == 0:
            print("It will take {} months to repay this loan!".format(periods))
        elif numYear == 1:
            print("It will take {} year to repay this loan!".format(numYear))
        else:
            if periods%12==0:
                print("It will take {} years to repay this loan!".format(numYear))
            else:
                periods = periods - (numYear*12)
                print("It will take {} years and {} months to repay this loan!".format(numYear,periods))
        overpayment = payment*periodsCopy - principal
        print("Total Interest = {}".format(round(overpayment,2)))

    if resultType == "a":

        principal = int(input(f"Enter the loan principal: "))
        princCheck(principal)

        periods = int(input(f"Enter the number of periods (months): "))
        periodCheck(periods)

        interest = float(input("Enter the loan interest: "))
        intCheck(interest)

        interest = (interest) / (12*100)
        raisedRate = math.pow(1+interest,periods)
        payment = math.ceil(principal * (interest*raisedRate)/(raisedRate-1))
        print("Your monthly payment = {}!".format(payment))
        overpayment = math.ceil(payment*periods - principal)
        print("Total Interest = {}".format(overpayment))

    if resultType == "p":

        payment = float(input("Enter the annuity payment amount: "))
        payCheck(payment)

        periods = int(input("Enter the number of periods (months): "))
        periodCheck(periods)

        interest = float(input("Enter the loan interest: "))
        intCheck(interest)

        interest = (interest) / (12*100)
        raisedRate = math.pow(1+interest,periods)
        principal = payment / ((interest*raisedRate)/(raisedRate-1))
        principal = math.floor(principal)
        print("Your loan principal = {}!".format(principal))
        overpayment = payment*periods - principal
        print("Total Interest = {}".format(overpayment))


if paymentType == "diff":
    principal = int(input(f"Enter the loan principal: "))
    princCheck(principal)

    periods = int(input(f"Enter the number of periods (months): "))
    periodCheck(periods)

    interest = float(input("Enter the loan interest: "))
    intCheck(interest)
    interest = (interest) / (12*100)
    overpayment=0
    for m in range(1,periods+1):
        payment = principal/periods + interest * (principal - principal*(m-1)/periods)
        payment = math.ceil(payment)
        print("Month {}: payment is {}".format(m,payment))
        overpayment = overpayment+payment
    print("Total Interest = {}".format(overpayment-principal))
