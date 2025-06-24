alumnos = []  # Lista vacía para guardar los nombres

while True:
    print("\n--- Menú de Alumnos ---")
    print("1. Agregar alumno")
    print("2. Mostrar todos los alumnos")
    print("3. Cerrar")
    
    opcion = input("Selecciona una opción (1-3): ")

    if opcion == "1":
        nombre_completo = input("Ingresa el nombre completo del alumno: ")
        primer_nombre = nombre_completo.strip().split()[0]  # Obtener solo el primer nombre
        alumnos.append(primer_nombre)
        print(f"Alumno '{primer_nombre}' agregado.")
    
    elif opcion == "2":
        print("\n--- Lista de Alumnos ---")
        if alumnos:
            for i, alumno in enumerate(alumnos, start=1):
                print(f"{i}. {alumno}")
        else:
            print("No hay alumnos registrados.")
    
    elif opcion == "3":
        print("Cerrando el programa...")
        break
    
    else:
        print("Opción inválida. Intenta nuevamente.")
