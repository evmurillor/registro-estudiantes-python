
estudiantes = {}


# Función para agregar estudiantes
def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    nota = float(input("Ingrese la calificación: "))

    estudiantes[nombre] = nota

    print("Estudiante agregado correctamente.\n")


# Función para mostrar todos los estudiantes
def mostrar_estudiantes():
    if len(estudiantes) == 0:
        print("No existen estudiantes registrados.\n")
    else:
        print("\n--- Lista de estudiantes ---")

        for nombre, nota in estudiantes.items():
            print(f"Nombre: {nombre} | Nota: {nota}")

        print()


# Función para buscar un estudiante
def buscar_estudiante():

    nombre = input("Ingrese el nombre a buscar: ")

    if nombre in estudiantes:
        print(f"{nombre} tiene una nota de {estudiantes[nombre]}\n")

    else:
        print("El estudiante no está registrado.\n")


# Función para eliminar estudiante
def eliminar_estudiante():

    nombre = input("Ingrese el nombre del estudiante a eliminar: ")

    if nombre in estudiantes:
        del estudiantes[nombre]
        print("Estudiante eliminado correctamente.\n")

    else:
        print("El estudiante no existe.\n")


# Menú principal
while True:

    print("===== REGISTRO DE ESTUDIANTES =====")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Eliminar estudiante")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_estudiante()

    elif opcion == "2":
        mostrar_estudiantes()

    elif opcion == "3":
        buscar_estudiante()

    elif opcion == "4":
        eliminar_estudiante()

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.\n")