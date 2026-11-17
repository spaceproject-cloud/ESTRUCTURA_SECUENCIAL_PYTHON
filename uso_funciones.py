import math

n = float(input("Ingrese el numero: "))

seno = math.sin(n)
coseno = math.cos(n)
tangente = math.tan(n)
raiz = math.sqrt(n) if n >= 0 else float("nan")
logaritmo_natural = math.log(n) if n > 0 else float("nan")
logaritmo_10 = math.log10(n) if n > 0 else float("nan")

print("El seno del numero es", seno)
print("El coseno del numero es", coseno)
print("La tangente del numero es", tangente)
print("La raiz cuadrada del numero es", raiz)
print("El logaritmo natural del numero es", logaritmo_natural)
print("El logaritmo 10 del numero es", logaritmo_10)
