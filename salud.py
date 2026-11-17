salario = float(input("Ingrese el salario base del empleado: "))

salud = salario * 0.04
pension = salario * 0.04
descuento = salud + pension
neto = salario - descuento

print("Salario base: $", salario)
print("Aporte a salud: $", salud)
print("Aporte a pension: $", pension)
print("Total de descuentos: $", descuento)
print("Salario neto a recibir: $", neto)
