print("Bienvenido al verificador de  rangos de Edad")
cant=int(input("Ingrese la cantidad de usuarios: "))

for i in range(cant):
    name=input("Ingrese su nombre: ")
    age=int(input("Ingrese su edad: "))

    if age<18:
        age_range="menor"

    elif age<=18 and age<=28:
        age_range="joven"

    elif age <= 29 and age <= 45:
        age_range = "señor"
    elif age <= 46 and age <= 100:
        age_range = "anciano"
    else:
        age_range = "Esta edad esta fuera del rango aceptado, lo sentimos"

    print(f"{name}, edad {age}: {age_range}.")