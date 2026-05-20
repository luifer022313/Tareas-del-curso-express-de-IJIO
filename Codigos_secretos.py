# Definir la lista de códigos secretos
codigos_secretos = [10, 25, 33, 42, 50]

# Intentar obtener el número del usuario
try:
    numero_usuario = int(input("Propón un número: "))

    # Comprobar si el número está en la lista
    if numero_usuario in codigos_secretos:
        print("ENCONTRADO")
    else:
        print("NO ESTÁ")

except ValueError:
    print("Error: Por favor, introduce un número entero válido.")
