#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt") as file:
    #de punt is vergelijkbaar met main.py, dus de plek waar dit bestand staat. Wil je vanuit deze map naar een ander
    #bestan in dezelfde map, dan moet je dus na de punt de nieuwe map noemen. Mik op leesbaarheid!
    letter = file.read()
    print(letter)

with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

for name in names:
    new = name.strip("\n")
    #gebruikt de gestripte naam in de definitieve brief
    #met de openfunctie kun je ook een nieuw bestand maken als dit nog niet bestaat
    with open(f"./Output/ReadyToSend/letter_for_{new}.txt", mode="w") as final:
        final.write(letter.replace(PLACEHOLDER, new))