# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# # #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_names = {
    row.letter : row.code for (index, row) in nato_data_frame.iterrows()
}
# print(nato_names)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter the word : ").upper()
# user_input_list = [n for n in user_input]
# result = []
# for i in user_input_list:
#     result.append(nato_names[i])
result = [nato_names[n] for n in user_input]

print(result)
