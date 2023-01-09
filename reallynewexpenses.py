# new expenses
total = 0
expenses = []
num_expenses = int(input("Enter # of expences"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)

print("You spent £", total, sep="")