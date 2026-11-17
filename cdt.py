dinero = float(input("Ingrese la cantidad de dinero que desea ingresar: "))
interes = float(input("Ingrese el porcentaje de intereses: "))
dias = float(input("Ingrese la cantidad de dias en el CDT: "))

# Se conserva la formula del algoritmo original de PSeInt.
valor_interes = (dinero * interes / 100 * dinero) / 360
print("Los intereses a pagar son:", valor_interes)

impuesto = valor_interes * 0.07
print("La cantidad de impuestos es:", impuesto)

pagar = dinero + valor_interes - impuesto
print("El neto a pagar es:", pagar)
