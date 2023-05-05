number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

if number2 > number1:
    largest_number = number2
    print(largest_number)
elif number3 > number2:
    largest_number = number3
    print(largest_number)
elif number1 > number3:
    largest_number = number1
    print(largest_number)
else:
    print("Ninguno")