
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
print("Dinner:\t",         menus["Dinner"]) #