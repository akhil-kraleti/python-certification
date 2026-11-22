import pandas as pd

#TODO 1. Create a dictionary in this format:
data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row_data.letter:row_data.code for (index,row_data) in data.iterrows() }
print(nato_dictionary)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Please enter a word: ")
letters_list = [letter.upper() for letter in user_input]
print(letters_list)
phonetic_list = [nato_dictionary[letter] for letter in letters_list ]
print(phonetic_list)

