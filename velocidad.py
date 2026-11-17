distancia = float(input("Ingresa la distancia: "))
tiempo = float(input("Ingresa tu tiempo (h): "))

if tiempo != 0:
    velocidad = distancia / tiempo
    print("Tu velocidad es", velocidad)
else:
    print("El tiempo no puede ser cero.")
