import random

# 1. Generar el número secreto aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)
intentos_totales = 3
ganado = False

print("He pensado un número entre 1 y 10. ¡Tienes 3 intentos para adivinarlo!")
print("---")

# 2. Bucle para controlar los 3 intentos
for intento in range(1, intentos_totales + 1):
    try:
        # Pedir el número al usuario
        propuesta = int(input(f"Intento {intento}/{intentos_totales}: "))
        
        # 3. Comprobar si adivinó o dar pistas
        if propuesta == numero_secreto:
            print("GANASTE")
            ganado = True
            break  # Rompe el bucle si gana, no necesita seguir intentando
        elif propuesta < numero_secreto:
            print("MÁS ALTO")
        else:
            print("MÁS BAJO")
            
    except ValueError:
        print("Eso no es un número válido (cuenta como intento).")

# 4. Condición final si se agotan los intentos
if not ganado:
    print("PERDISTE")
    print(f"El número secreto era el {numero_secreto}.")
