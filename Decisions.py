#  Weather
#  6 Comparators in Python
#  < less than
#  <= less than equal to
#  == equal to
#  greater than equal to
#  greater than
#  != NOT equal

temperature = 95
if temperature > 80:
    print("Its too hot!")  # Code Block
    print("Stay inside!")


temperature = 75
if temperature > 80:
    print("Its too hot!")  # Code Block
    print("Stay inside!")
print("Have a good day!")


#  Adding the else
temperature = 75
if temperature > 80:
    print("Its too hot!")  # Code Block
    print("Stay inside!")
else:
    print("Enjoy the outdoors!")



#  Adding the elif for less than 60
temperature = 50
if temperature > 80:
    print("Its too hot!")  # Code Block
    print("Stay inside!")
elif temperature < 60:
    print("Its too cold!")
    print("Stay inside!")
else:
    print("Enjoy the outdoors!")


#  Adding the or statement
temperature = 75
if temperature > 80 or temperature < 60:
    print("Stay inside!")
else:
    print("Enjoy the outdoors!")

#  Change the temp to make sure it catches
temperature = 90
if temperature > 80 or temperature < 60:
    print("Stay inside!")
else:
    print("Enjoy the outdoors!")

#  And lets you combine multiple comparisons but both need to be True for the whole statement to be True
temperature = 75
forecast = "rain"
if temperature < 80 and forecast != "rain":
    print("Go Outside!")
else:
    print("Stay inside!")

#  Update forecast to be sunny
temperature = 75
forecast = "sunny"
if temperature < 80 and forecast != "rain":
    print("Go Outside!")
else:
    print("Stay inside!")

#  Logical Operator - not
forecast = "rain"
if not forecast == "rain":
    print("Go Outside!")
else:
    print("Stay inside!")

#  Update forecast
forecast = "sunny"
if not forecast == "rain":
    print("Go Outside!")
else:
    print("Stay inside!")

#  boolean - True or False

raining = True
if raining:
    print("Stay inside!")

raining = True
if not raining:
    print("Go outside!")
else:
    print("Stay inside!")

# This is from pluralsight
