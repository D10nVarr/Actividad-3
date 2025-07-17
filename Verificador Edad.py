elif 29 <= edad <= 45:
        etapa = "señor"
    elif 46 <= edad <= 100:
        etapa = "anciano"
    else:
        etapa = "Esta edad esta fuera del rango aceptado, lo sentimos"
    print(f"{nombre}, edad {edad}: {etapa}.")
