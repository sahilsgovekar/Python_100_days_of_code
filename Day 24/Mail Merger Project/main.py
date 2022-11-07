#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


names = []
with open("./input/Names/invited_names.txt") as inn:
    invited_names = inn.read()
    names = invited_names.split()


with open("./input/letters/starting_letter.txt") as sl:
    starting_letter = sl.read()
    for i in names:
        output_letter = starting_letter.replace("[name]", i)
        with open(f"./Output/ReadyToSend/outputletter {i}", "w") as ol:
            ol.write(output_letter)
