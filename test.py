from Source import ExpenseCalculator

expense_calc = ExpenseCalculator("./Data/expenses.csv")

amount = input("What is the amount that you spent: ")
time = input("What is the time that you spent: ")
type = input("What is the type of the spending: ")
expense_calc.log(amount, time, type)

print(expense_calc._expenses)