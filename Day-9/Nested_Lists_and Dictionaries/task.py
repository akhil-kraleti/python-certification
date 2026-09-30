capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nested list in dictionary
travel_log = {
    "France": ["Paris","Lille","Bijon"],
    "Germany": ["Berlin","Stuttgart"],
}

#print lille
print(travel_log["France"][1])

#Nested lists
nested_list = ["A","B",["C","D"]]
print(nested_list[2][1])

#Nested dictionaries
travel_log = {
    "France": {
        "total_visits":8,
        "cities_visited": ["Paris","Lille","Bijon"],
    },
    "Germany": {
        "cities_visited":["Berlin","Stuttgart"],
        "total_visits":12,
    },
}

print(travel_log["Germany"]["cities_visited"][1])

