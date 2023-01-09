

#  Get the loan details
money_owed = float (input("How much money do you owe, in pounds?\n")) # 50,000
apr = float(input("What is the annual percentage rate?\n")) # 3%
payment = float(input("What will your monthly payment be, in pounds?\n")) # 1,000
months = int(input("How many months do you want to see results for?\n")) # 24

# Divide apr by 100 to make it a percent, then divide by 12 to make monthly
monthly_rate = apr/100/12

# Add interest
interest_paid = money_owed * monthly_rate
money_owed = money_owed + interest_paid

# Make payment
money_owed = money_owed - payment

# Print the results after this month
print("Paid", payment, "of which", interest_paid, "was interest.", end=" ")
print("Now I owe", money_owed)