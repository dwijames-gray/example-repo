####Psuedo Code
#1. User is greeted with a message on investment and bond information and is asked to choose between these
#2a. If investment user is  asked to input deposit, interest and years (rate is calculated from interest)
#2aa. User asked what interest type for investment.
#2ab. Depending on user choice on interest type, user is given the total investment sum.
#2b. If bond is selected user is asked to input bond value, interest and duration in months of bond
#2ba. User is then provided with monthly repayments from the informaiton provided 



#libraries imported
import math as m #alias created



#Welcome message to the user
print("Investment - to calculate the amount of interest you'll earn on your investment.\n" 
      "Bond       - to calculate the amount you'll have to pay on a home loan. ")
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed:")
choice = choice.lower() #converts all characters into lower-case so user input is not case sensitive

#lets the user know if their choice is invalid with a user-friendly message
if choice != "investment" and choice != "bond":  
   print("Please select either 'investment' or 'bond'.") 

#elif instead to ensure only one condition runs
elif choice == "investment":
    try:   #try is used with except to inform the user of any invalid characters
        deposit = float(input("Please provide amount of money being deposited:"))  #asks the user to insert deposit will only accept numbers
        interest = float(input("Please provide the interest rate:"))  #asks the user to insert interest will only accept numbers
        rate = interest / 100  ### This is used in the calculation but is skipped in the investment details below
        years = int(input("Number of Years of Investment:"))  #asks user to insert number of years of investment

        #print Investment details in a readable format   
        print("____________________\n", 
              "Investment Details\n", 
              f"Deposit:  {deposit}\n", 
              f"Interest: {interest} %\n", 
              f"Years:    {years}")

        #asks user to input the interest type
        interest_type = input("Please enter the interest type (Simple or Compound): ") 
        interest_type = interest_type.lower()  #converts all characters into lower-case so user input is not case sensitive

        #Calculates the interest type and then prints the amount to the user. 
        if interest_type == "simple":  #if statement is used here as this is expanding on the current condition by gaining new info.
            simple_interest = deposit * (1 + rate * years)  #simple interest calculation
            simple_interest = round(simple_interest, 2)  #rounds this after
            print(f"Amount gained from Simple Interest £{simple_interest}")
        elif interest_type == "compound":  #elif used here as this is another condition for interest type
            compound_interest = deposit * m.pow((1 + rate), years)  #compund interest calculation
            compound_interest = round(compound_interest, 2)
            print(f"Amount gained from Compound Interest £{compound_interest}")
        else:
            print("Please choose between 'Simple' or 'Compound'.")  #message if user inputs anything else other than these conditions

    except ValueError:  #except is used to print the error in a user-friendly way
        print("Invalid Input Detected - Please Only Insert Numbers")


#If user selects bond, they are then prompted to add bond information
elif choice == "bond": #elif  instead of if part of same condition between choosing investment or bond
    try: #try is used with except to inform the user of any invalid characters
        bond_value = float(input("Please enter the bond value: "))
        interest = float(input("Please provide the interest rate:"))
        rate = (interest / 100) / 12 #not provided in the bond details below, used for the calculation
        monthly_duration = int(input("Please provide duration in months of repayment plan:"))
        #bond details information inputted by user in a user-friendly format
        print("____________________\n", 
            "Bond Details\n" 
            f"Deposit:           £{bond_value}\n"
            f"Interest:          {interest}%\n"
            f"Number of Months: {monthly_duration}")
        repayment = (rate * bond_value) / (1 - (1 + rate)**(-monthly_duration)) #repayment calculation
        repayment = round(repayment, 2) 
        print(f"Monthly Bond Repayment: £{repayment}") #prints bond repayment to the user
    except ValueError:  #except is used to print the error in a user-friendly way
        print("Invalid Input Detected - Please Only Insert Numbers")


# Possible improvment - add a  loop so the user can start again if a error is made. 
