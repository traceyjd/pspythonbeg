# new expenses
total = 0
expenses = []
for i in range(7):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)

print("You spent £", total, sep="")


# This is from pluralsight