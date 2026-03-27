nombre = input("¿Cuál es tu nombre? ")
salario = int(input("¿Cuál es tu salario mensual (COP)? "))
gasto_mercado = int(input("¿Cual es el gasto del mercado mensual (COP)? "))
gasto_arriendo = int(input("¿Cual es el gasto del arriendo mensual (COP)? "))
gasto_transporte = int(input("¿Cual es el gasto del transporte mensual (COP)? "))
gastos = gasto_mercado + gasto_arriendo + gasto_transporte

saldo_final = salario - gastos
porcentaje_gastado = (gastos / salario) * 100

if porcentaje_gastado <= 50:      
    estado = "Vas muy bien, estás ahorrando bastante"
elif porcentaje_gastado <= 80 :
    estado = "Va bien pero puedes mejorar"
elif porcentaje_gastado <=  100:
    estado = "Cuidado, casi no te queda nada"
else: 
    estado = "⚠ ALERTA: Estás gastando más de lo que ganas"

print("=" * 30)
print("===== Resumen Financiero =====")
print(f"Nombre: {nombre}")
print(f"Salario: ${salario:,}")
print(f"Gastos totales: ${gastos:,}")
print(f"Saldo disponible: ${saldo_final:,}")
print(f"Porcentaje gastado: {porcentaje_gastado:.2f}%")
print(f"Estado: {estado}")
print("=" * 30)