num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

if num2 != 0:
    resultado = num1 % num2
    print("El modulo es:", resultado)
else:
    print("No se puede calcular el modulo entre cero.")
