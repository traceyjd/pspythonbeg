
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