user_word = input("Ingrese una palabra: ")
user_word = user_word.upper()
print("Palabra ingresada: ", user_word, "\n")
word_without_vowel = ""

for letter in user_word:
    if letter == "A":
        word_without_vowel += letter
        continue
    elif letter == "E":
        word_without_vowel += letter
        continue
    elif letter == "I":
        word_without_vowel += letter
        continue
    elif letter == "O":
        word_without_vowel += letter
        continue
    elif letter == "U":
        word_without_vowel += letter
        continue
    else:
        print(letter)
        
print(word_without_vowel)
        