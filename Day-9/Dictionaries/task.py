programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
    123:"Numbers",
}

#Accessing elements by key values
print(programming_dictionary["Bug"])
print(programming_dictionary[123])

#Adding new elements to the dictionary
programming_dictionary["ABC"] = "Alphabets."
print(programming_dictionary)

#Deleting the content of a dictionary
programming_dictionary={}
print(programming_dictionary)

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
    123:"Numbers",
}

#Edit an item in the dictionary
programming_dictionary["Bug"]="A moth in your computer"
print(programming_dictionary)

#Looping on a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])