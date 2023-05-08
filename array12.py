beatles = []
print("Paso 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

for i in range(2):
    m = input("Agrege el miembro faltante: ")
    beatles.append(m)
print("Paso 3:", beatles)

del beatles[3]
beatles.pop()
print("Paso 4:", beatles)

beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))

