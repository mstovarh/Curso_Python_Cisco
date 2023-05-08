palabraSecreta = "chupacabra"
counter = 0

while counter != -1:
    palabra = input("Ingresa una palabra: ")
    if palabra == "chupacabra":
        print("Has dejado el bucle con éxito.")
        break
    counter += 1