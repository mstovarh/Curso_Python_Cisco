user_word = input("Ingrese una palabra: ")
user_word = user_word.upper()
print("Palabra ingresada: ", user_word, "\n")

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)
