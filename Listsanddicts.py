
#  Breakfast lunch and dinner

# In python you can have a container of contrainers - menus is a list of lists.

menus = [ ["Egg Sandwich", "Bagel", "Coffee"],
          ["BLT", "PB&J", "Turkey SAndwich"],
          ["Soup", "Salad", "Spaghetti", "Taco"]]

print("Breakfast Menu:\t", menus[0])
print("Lunch:\t",          menus[1])
print("Dinner:\t",         menus[2])

#  But how do you get an individual item from an inner list??? Good question???

menus = [ ["Egg Sandwich", "Bagel", "Coffee"],
          ["BLT", "PB&J", "Turkey SAndwich"],
          ["Soup", "Salad", "Spaghetti", "Taco"]]

print(menus[0][1])

# You can also use a dictionary for our menus with keys for Breakfast Lunch and Dinner

menus = { "Breakfast" : ["Egg Sandwich", "Bagel", "Coffee"],
          "Lunch" : ["BLT", "PB&J", "Turkey SAndwich"],
          "Dinner" :  ["Soup", "Salad", "Spaghetti", "Taco"]}

print("Breakfast Menu:\t", menus["Breakfast"]) # Using the keys to access each list
print("Lunch:\t",          menus["Lunch"])
print("Dinner:\t",         menus["Dinner"])

# Above we have all the menus printed on different lines but is there a better way of doing this? Yup you bet

# Using a for loop to print the menu items

menus = { "Breakfast" : ["Egg Sandwich", "Bagel", "Coffee"],
          "Lunch" : ["BLT", "PB&J", "Turkey SAndwich"],
          "Dinner" :  ["Soup", "Salad", "Spaghetti", "Taco"]}

for item in menus:
    print(item) # this defaults to just printing the keys in the menus, BUT WE WANT THE VALUES TOO, FEAR NOT DEAR FRIEND


menus = { "Breakfast" : ["Egg Sandwich", "Bagel", "Coffee"],
          "Lunch" : ["BLT", "PB&J", "Turkey SAndwich"],
          "Dinner" :  ["Soup", "Salad", "Spaghetti", "Taco"]}

for name, menu in menus.items(): # Now the loop has access to both the key and the value here
    print(name, ":", menu)

