elif 29 <= age <= 45:
etapa = "señor"
elif 46 <= age <= 100:
etapa = "anciano"
else:
etapa = "Esta edad esta fuera del rango aceptado, lo sentimos"

print(f"{name}, edad {age}: {etapa}.")