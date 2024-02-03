from time import sleep
name = "Alex"
last_name = "Mindota"
address = "afghanisan"
contact_no = "093939393"
addressBook = [  ]

person1 = {
    "first_name": name,
    "last_name": last_name,
    "address": address,
    "contact_no": contact_no
}
person2 = {
    "first_name": "jomari",
    "lastn_name":"snake",
    "address": address,
    "contact_no": contact_no
}

# Add person1 and person2 to address book
addressBook.append(person1)
addressBook.append(person2)

# # View Contacts
# print("veiwing contacts", end = "")
# for i in range(5):
#     sleep(1)
#     print(".", end= "")
# print("O")
# print("")

# for i, person in enumerate(addressBook):
#     print(f"{i+1}. {person["first_name"]} #{person["contact_no"]}")

# print("")

print(addressBook)