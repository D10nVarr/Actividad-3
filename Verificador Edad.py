print("Bienvenido al verificador de  rangos de Edad")
cant=int(input("Ingrese la cantidad de usuarios: "))

for i in range(cant):
    name=input("Ingrese su nombre: ")
    age=int(input("Ingrese su edad: "))

    if age<18:
        age_range="menor"

    elif age<=18 and age<=28:
        age_range="joven"