import pandas

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_names = {
    row.letter : row.code for (index, row) in nato_data_frame.iterrows()
    }

def nato():
    user_input = input("Enter the word : ").upper()
    try:
        result = [nato_names[n] for n in user_input]
    except KeyError:
        print("Please enter only alphabet")
        nato()
    else:
        print(result)


nato()
