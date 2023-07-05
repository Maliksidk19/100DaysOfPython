import os

with open("Files/starting_letter.txt") as letter_starting:
    names = []
    letter = letter_starting.read()
    with open("Files/invited_names.txt", "r") as names_list:
        for name in names_list:
            names.append(name.replace('\n', ''))
        names_list.close()
    os.mkdir("Files/Output_Files")
    for name in names:
        with open(f"Files/Output_Files/{name}.txt", 'w') as letter_final:
            letter_final.write(letter.replace('[name]', name))
            letter_final.close()
    letter_starting.close()
    
    
