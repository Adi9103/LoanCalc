import math
import argparse

parser = argparse.ArgumentParser(description = "loan calculator")
parser.add_argument("--type", choices= ["annuity", "diff"], help="Enter annuity of diff")
parser.add_argument("--payment", help = "Monthly payment amount", type=int)
parser.add_argument("--principal", help = "Loan amount", type=int)
parser.add_argument("--periods", help = "Loan period in months", type=int)
parser.add_argument("--interest", help = "Annual interest rate", type=float)

    
def diffCalc(principal, interest, periods, payment):
    if interest is None or payment is not None:
        print("Incorrect parameters.")
        exit()
    if (interest <0) or (principal <0) or (periods <0):
        print("Incorrect parameters.")
        exit()
    interest = (interest) / (12*100)
    overpayment=0
    for m in range(1,periods+1):
        payment = principal/periods + interest * (principal - principal*(m-1)/periods)
        payment = math.ceil(payment)
        print("Month {}: payment is {}".format(m,payment))
        overpayment = overpayment+payment
    print("Overpayment = {}".format(overpayment-principal))
    
def annuityCalc(principal, interest, periods, payment):
    if interest is None:
        print("Incorrect parameters.")
        exit()
    if payment is None:
        interest = (interest) / (12*100)
        raisedRate = math.pow(1+interest,periods)
        payment = math.ceil(principal * (interest*raisedRate)/(raisedRate-1))
        print("Your monthly payment = {}!".format(payment))
        overpayment = math.ceil(payment*periods - principal)
        print("Overpayment = {}".format(overpayment))
    if principal is None:
        interest = (interest) / (12*100)
        raisedRate = math.pow(1+interest,periods)
        principal = payment / ((interest*raisedRate)/(raisedRate-1))
        principal = math.floor(principal)
        print("Your loan principal = {}!".format(principal))
        overpayment = payment*periods - principal
        print("Overpayment = {}".format(overpayment))
    if periods is None:
        interest = (interest) / (12*100)
        inLog = payment / (payment - interest*principal)
        periods = math.log(inLog, 1+interest)
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
        overpayment = payment*periods - principal
        print("Overpayment = {}".format(overpayment))
    
    
args = parser.parse_args()
if args.type is None:
    print("incorrect parameters")
    exit()
if args.type == "diff":
    diffCalc(args.principal, args.interest, args.periods, args.payment)
    
    
if args.type == "annuity":
    annuityCalc(args.principal, args.interest, args.periods, args.payment)