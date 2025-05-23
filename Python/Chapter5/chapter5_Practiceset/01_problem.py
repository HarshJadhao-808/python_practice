
print("\t\t\t\t\t\tWelcome to my dictionary \n\n")


Words={
    "Aadmi":"Man",
    "Chai":"Tea",
    "Bhasha":"Language",
     "pani": "water",
    "aag": "fire",
    "dharti": "earth",
    "aasmaan": "sky",
    "sooraj": "sun",
    "chaand": "moon",
    "ped": "tree",
    "patta": "leaf",
    "billi": "cat",
    "kutta": "dog"
}

print("These are some words you can find meaning in English\n\n\t\t\t" , Words.keys())


word=input("Enter your wordhere :")

print("Ok so your word is ", word, "\n\n\t The meaning of ", word ,"is ",(Words[word]))


