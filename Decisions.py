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

