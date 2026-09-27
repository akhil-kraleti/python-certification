#Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Akhil","Vizag")
greet_with(location="vizag",name="Akhil")