import os
import sys
import datetime

### Hej!
class UltimateTracker():
    def __init__(self):
        self.dateNow = datetime.date.today()
        self.budget = 0
        self.budget_list = []
        self.totalbudget = 0
        self.expenses = 0
        # self.expenses = 0
        # self.expense_list = []
        # self.expense_name = []
        # self.income_name = []
        # self.income_list = []
        self.mainMenu()

    def mainMenu(self):

        print("\n\n\n****** WELCOME TO ULTIMATE TRACKER ******\n")
        print("What do you want to do today?:")

        print("\n")

        try:

            print("1 = SET BUDGET")
            print("2 = SET RECIPE")
            print("3 = SEE BALANCE******")
            print("4 = HISTORY")
            print("5 = EXIT")

            selection = int(input("Enter choice: "))

            if selection == 1:
                self.setBudget()
            elif selection == 2:
                setRecipeCost()
            elif selection == 3:
                bad()
            elif selection == 4:
                self.seeHistory()
            elif selection == 5:
                exit
            else:
                print("invalid")
                self.mainMenu()
        except:
            print("Write a number from 1-6 \n")
            self.mainMenu()

    def setBudget(self):
        self.budget = float(input("Please enter your budget today: "))

        try:

            if self.budget <= 0:
                print("Please be serious and enter your budget for today!")
                self.setBudget()
            else:

                # "SPARA BUDGETEN I PROGRAMMET SÅ DEN KAN FÖLJA MED?"
                self.budget_list.append(self.budget)

                # Lägg till i TOTALT(expenses)
                self.income_sum()

                print(self.budget, "kr || Budget has been added! ",
                      self.dateNow, "\n\n")
        except:
            print("Please enter your budget!\n")
            self.setBudget()

        self.mainMenu()

    def income_sum(self):
        self.expenses = sum(self.budget_list)

    def setRecipeCost():

        #"KUNNA LÄGGA IN KATEGORI I KVITTON"

        recipe = float(input("Please Enter the cost of your Recipe: "))


#Summa på kvitto, kategori, datum, skillnaden i summan(ifall
# man har överstigit sin budget eller inte), Budget***

#"Budget på Alla tidigare dagar + eller - "
    def seeHistory(self):

        ########### KAN INTE FÅ FRAM HISTORIK #########

        for k in self.budget_list:
            print(k + " ", " kr " + str(k))

        print("Total: ", str(self.expenses) + " kr")

        #print("This is your history: \n")
        #print (self.budget_list)

        #self.mainMenu()


if __name__ == '__main__':

    UltimateTracker()

expense = 0.0
budget = 0.0
difference = 0.0
expenseTotal = 0.0

total_expense = 0
keep_going = 'y'

#Input Module
budget = float(input("What is your budget for the month?"))
print("Please begin entering the amounts of each of your monthly expenses:")

while keep_going == 'y':
    expense = float(input("Monthly expense amount? $"))
#*Having an issue keeping the expense running total at the end of the program?*
    total_expense = total_expense + expense
    keep_going = input("Do you have any other expenses? (Enter y for yes.)")

#Calculations Module
if expense < budget:
    difference = budget - expense
    print("You were $", difference, " under budget.")

elif expense > budget:
    difference = expense - budget
    print("You were $", difference, " over budget.")

else:
    print("You were right on budget. Great Job!!!")

input("Press enter to exit.")
