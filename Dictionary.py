

acronyms = {}

acronyms["LOL"] = "Laugh out loud" # Adding in values to our empty list
acronyms["IDK"] = "I don't know"
acronyms["TBH"] = "To be honest"

# Adding items
acronyms["TBH"]  = "honestly"# A value is updated the same way a value is added

print(acronyms)

#  Notice that our 3 key-value pairs are there but order is random in a dictionary

# Removing items - remove items by looking up the key

acronyms = {}

acronyms["LOL"] = "Laugh out loud" # Adding in values to our empty list
acronyms["IDK"] = "I don't know"
acronyms["TBH"] = "To be honest"

del acronyms["LOL"]

print(acronyms)

#  Get an item that might not be there
acronyms = {}

acronyms["LOL"] = "Laugh out loud" # Adding in values to our empty list
acronyms["IDK"] = "I don't know"
acronyms["TBH"] = "To be honest"

definition = acronyms.get("BTW") # Using get wont crach your program
print(definition)

# None

# None is returned to show the absence of a value and also evaluates to false in a conditional

acronyms = {}

acronyms["LOL"] = "Laugh out loud" # Adding in values to our empty list
acronyms["IDK"] = "I don't know"
acronyms["TBH"] = "To be honest"

definition = acronyms.get("BTW") # Using get wont crach your program

if definition:
    print(definition)
else:
    print("Key does not exisit")