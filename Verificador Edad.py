print("Bienvenido al verificador de  rangos de Edad")
cant=int(input("Ingrese la cantidad de usuarios: "))

for i in range(cant):

    age=int(input("Ingrese su edad: "))

    if age<18:
        print("Usted es considerado un menor de edad")