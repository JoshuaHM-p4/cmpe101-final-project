name = "Alex"
last_name = "Mindota"
address = "afghanisan"
contact_no = "Pres of the United States"

addressBook = [
    {
        "first_name": name,
        "last_name": last_name,
        "address": address,
        "contact_no": contact_no
    },
    {
        "first_name" : "Jomari",
        "last_name": "Mangahas",
        "address": address,
        "contact_no": contact_no
    }
]

# Delete concept
# del addressBook[0]["first name"]
# addressBook[0]["first name"] = "New Name Alex"
# print(addressBook)

# Search Concept 
prompt = "Jomari"
found = ""

for person in addressBook:
    if person["first_name"] == prompt:
        found = person

print(found)