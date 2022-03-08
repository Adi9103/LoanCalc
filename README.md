# LoanCalc
LoanCalc is a program written in Python that calculates financial info based on the information that the user provides. 

## User Input Version (NOW AVAILABLE)
This version of the program takes user input after the program is run. This works by entering letters that trigger different scenarios in the program. This is designed for beginners with no prior knowledge of programming
### Usage
After running the program, follow the instructions.  
Ex:

```console
> python3 LoanCalcSimple.py
Annuity Payment: Type "annuity"
Differentiated Payment: Type "diff
```

## Command Line Argumentation Version
This version of the program takes input in the command line interface before the program is run. This makes it easier for a user with a programming background to use the program. This is used with the Python module ```argparse```. 
### Usage
While running the program, include arguments.  
Ex: 
```console
> python3 LoanCalcluator.py --type=diff --principal=1000000 --periods=10 --interest=10
Month 1: payment is 108334
Month 2: payment is 107500
Month 3: payment is 106667
Month 4: payment is 105834
Month 5: payment is 105000
Month 6: payment is 104167
Month 7: payment is 103334
Month 8: payment is 102500
Month 9: payment is 101667
Month 10: payment is 100834
Total Interest = 45837
```
 If there are any doubts, use the ```--help``` flag.
