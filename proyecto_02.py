import random

ganadas = 0
perdidas = 0

def jugar(limite, intentos_max):
    numero = random.randint(1, limite)
    intentos = intentos_max
    gano = False
    
    
    while intentos > 0:
        adivina = int(input(f"Adivina el número entre 1 y {limite}: "))
        if adivina == numero:
            print(f"¡Correcto! Lo lograste en {intentos_max - intentos + 1} intento(s).")
            gano = True
            return True
        else:
            intentos -= 1
            print(f"Incorrecto. Te quedan {intentos} intentos.")
            if numero < adivina:
                print("El número es menor")
            else:
                print("El número es mayor")

    
    print(f"Perdiste. El número era {numero}")
    return False




jugando = True

while jugando:

    print("\n===== BIENVENIDO AL JUEGO DE ADIVINANZA =====")
    print("1. Fácil     (1-10, 5 intentos)")
    print("2. Medio     (1-50, 4 intentos)")
    print("3. Difícil   (1-100, 3 intentos)")
    print("4. Salir")

    opcion = int(input("Seleccione dificultad: "))

    if opcion == 1:
        if jugar(10,5):
            ganadas += 1
        else:
            perdidas += 1

    elif opcion == 2:
        if jugar(50, 4):
            ganadas += 1
        else:
            perdidas += 1

    elif opcion == 3:
        if jugar(100, 3):
            ganadas += 1
        else:
            perdidas += 1

    elif opcion == 4:
        break

    else:
        print("Opción no válida")
        continue

    # Preguntar si quiere seguir
    while True:
        decision = input("¿Quieres seguir jugando? (s/n): ").lower()

        if decision == "n":
            jugando = False
            break
        elif decision == "s":
            break
        else:
            print("Escribe 's' o 'n'.")

print("=" * 30)
print("ESTADÍSTICAS FINALES")
print(f"Ganadas:  {ganadas}")
print(f"Perdidas: {perdidas}")
print("¡Gracias por jugar!")

