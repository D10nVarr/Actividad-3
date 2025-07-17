elif 29 <= age <= 45:
  = "señor"
elif 46 <= age <= 100:
 age_range = "anciano"
else:
 age_range = "Esta edad esta fuera del rango aceptado, lo sentimos"

print(f"{name}, edad {age}: {age_range}.")