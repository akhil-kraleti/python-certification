#Lists Data Type
states_of_india = ["Andhra Pradesh","Arunachal Pradesh","Telangana","Tamil Nadu","Karnataka","Madhya Pradesh"]

#accessing elements in a list
print(states_of_india[0])
print(states_of_india[1])
print(states_of_india[-1])

#list is mutable
states_of_india[1]="Assam"

#adding new element at the end of the list
states_of_india.append("Panjab")

#adding a list of new elements at the end of the existing list
states_of_india.extend(["Rajasthan","Uttar Pradesh"])

#deleting an element using its index value
states_of_india.pop(2)

print(states_of_india)