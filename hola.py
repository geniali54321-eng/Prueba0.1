lista_entrenadores = []  # Lista vacía para guardar gente (Requisito C)
contador = 0             
#Para mantener el bucle
while True:
    print("\n--- Nuevo Registro ---")
    
    # Parte 1: Pedir datos y controlar errores (Requisito D)
    #Aqui pido los datos
    try:
        nombre = input("Nombre: ")
        pokemon = int(input("¿Cuántos Pokemon tienes?: "))
        heridos = int(input("¿Cuántos heridos?: "))
        experiencia = int(input("Experiencia (puntos): "))
    except ValueError:
        print("¡Error! Debes poner números.")
        continue  # Vuelve al principio del while

    tarjeta = input("¿Tarjeta válida? (S/N): ").upper()

    # Parte 2: Uso del PASS (Requisito D)
    if pokemon == 0 and tarjeta == "N":
        pass  # No hace nada, ignora al entrenador
    else:
        # Tu lógica original de clasificación
        if pokemon == 0:
            print("Rango: Nuevo")
        elif pokemon <= 2:
            print("Rango: Principiante")
        elif pokemon <= 5:
            print("Rango: Intermedio")
        else:
            print("Rango: Experto")

        # Guardamos al entrenador en la lista (Requisito C)
        lista_entrenadores.append([nombre, experiencia])
        contador = contador + 1

    # Parte 3: Salir (Requisito B)
    opcion = input("¿Escribe 'salir' para terminar o ENTER para seguir?: ")
    if opcion == "salir":
        break  # Rompe el bucle y termina el registro

# Parte 4: Buscar al experto (Requisito E)
print("\n--- Buscando Entrenador Élite ---")

for entrenador in lista_entrenadores:
    exp = entrenador[1]  # La experiencia es el segundo dato guardado
    
    if exp > 5000:
        print("¡Tenemos un entrenador élite en el sistema!")
        break  # Para de buscar si encuentra uno
else:
    # Este 'else' pertenece al 'for', se ejecuta si NO hubo 'break'
    print("No se han encontrado entrenadores élite.")

print(f"Total atendidos: {contador}")