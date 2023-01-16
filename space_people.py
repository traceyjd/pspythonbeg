# Using JSON and PIP

# We want a program that lists the current people in space

# Some websites return raw data - Usually the raw data is returned under the API (Application Programming Interface)
# for the website sucha s api.twitter.com

# JSON Data is a common way to exchange data to/from a web server.

# json = {
#     "number":4,
#     "students":
#     [
#         {"name":"Tracey Doogan", "email":"tracey@example.com"},
#         {"name":"Joe Doogan", "email":"joe@example.com"},
#         {"name":"Nellie Doherty", "email":"nellie@example.com"},
#        {"name":"Bob Doherty", "email":"bob@example.com"},
# #    ]
# #}
# JSON is typically a mix of Lists and dictionaries like we've been using above
#
# JSON stands for JavaScript Object Notation

import requests

response = requests.get("http://api.open-notify.org/astros.json")
json = response.json()
print(json)

# To access just the persons name

import requests

response = requests.get("http://api.open-notify.org/astros.json")
json = response.json()

print("The people currently in space are:")
for person in json["people"]:
    print(person["name"])



