# empty list
empty = []

# list of strings
# acronyms = ["LOL", "IDK", "TBH"]

# lists of numbers
#numbers = [5, 10, 15, 20]

# list of mixed items
#anything = [5, "SDK", 10.5]

# list of lists
#lists = [ ["A", "B", "C"], ["D", "E", "F"] ]

# append - adding items to a list
acronyms.append("LOL")
acronyms.append("IDK")

# removing items - or use del
acronyms.remove("IDK")
print(acronyms)

del acronyms [1]
print(acronyms)

# check if exists in list
acronyms = ["LOL", "IDK", "TBH", "SMH"]
word = "BFN"
if word in acronyms:
    print(word + " is in the list")
else:
    print(word + " is NOT in the list")

#  Do this block of code for each string acronym in the acronyms list
acronyms = ["LOL", "IDK", "TBH", "SMH"]
for acronyms in acronyms:
    print(acronyms)

# This is from pluralsight


