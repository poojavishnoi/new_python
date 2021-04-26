
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())
#TODO 1. Create a dictionary in this format:
dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter the name:\n").upper()
output_list = [dict[letter] for letter in user_input]
print(output_list)