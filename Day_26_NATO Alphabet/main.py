# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# # for (key, value) in student_dict.items():
# #     print(value)
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# # for (index, row) in student_data_frame.iterrows():
# #     print(row)
#
# # Keyword Method with iterrows()
# new_df = {row.student:row.score for (index, row) in student_data_frame.iterrows()}
# print(new_df)

# #TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
import pandas
nato = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}

#Leerpunt: mijn code werkte niet omdat ik uit diverse rijen informatie probeerde te halen. Row.letter en row.code
#halen input uit dezelfde rij.
#
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input = input("What word would you like to spell in NATO Phonetic Alphabet? \n").upper()
output = [nato_dict[letter] for letter in input]
print(output)



