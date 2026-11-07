from funciones import (
    leer_texto,
    leer_entero,
    leer_numero,
    guardar_proyectos,
    cargar_proyectos,
    guardar_usuarios,
    cargar_usuarios
)

from estadistica import seleccionar_datos


def registrar_usuario(usuarios):
    print("\nREGISTRO")

    nombre = leer_texto("Ingrese un nombre de usuario: ")
    clave = leer_texto("Ingrese una clave: ")

    existe = False

    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            existe = True

    if existe:
        print("Ese usuario ya existe.")
    else:
        usuario = {
            "nombre": nombre,
            "clave": clave
        }

        usuarios.append(usuario)
        guardar_usuarios(usuarios)
        print("Usuario registrado correctamente.")


def iniciar_sesion(usuarios):
    print("\nINICIAR SESION")

    intentos = 0
    acceso = False

    while intentos < 3 and not acceso:
        nombre = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        for usuario in usuarios:
            if usuario["nombre"] == nombre and usuario["clave"] == clave:
                acceso = True

        if acceso:
            print("Acceso correcto.")
        else:
            intentos = intentos + 1
            print("Usuario o clave incorrectos.")

    if not acceso:
        print("Supero la cantidad de intentos.")

    return acceso


def crear_proyecto(proyectos):
    nombre = leer_texto("Nombre del proyecto: ")

    proyecto = {
        "nombre": nombre,
        "tablas": []
    }

    proyectos.append(proyecto)
    guardar_proyectos(proyectos)

    print("Proyecto creado correctamente.")


def mostrar_proyectos(proyectos):
    if len(proyectos) == 0:
        print("No hay proyectos.")
    else:
        print("\nPROYECTOS")

        for i in range(len(proyectos)):
            print(i + 1, "-", proyectos[i]["nombre"])


def elegir_proyecto(proyectos):
    if len(proyectos) == 0:
        print("No hay proyectos.")
        return None

    mostrar_proyectos(proyectos)

    opcion = leer_entero("Seleccione un proyecto: ", 1, len(proyectos))

    return proyectos[opcion - 1]


def crear_tabla(proyectos):
    proyecto = elegir_proyecto(proyectos)

    if proyecto != None:
        nombre = leer_texto("Nombre de la tabla: ")

        tabla = {
            "nombre": nombre,
            "columnas": [],
            "filas": []
        }

        cantidad = leer_entero("Cantidad de variables: ", 1, 20)

        for i in range(cantidad):
            print("\nVariable", i + 1)

            nombre_variable = leer_texto("Nombre: ")

            print("1. Texto")
            print("2. Numero")

            tipo = leer_entero("Seleccione el tipo: ", 1, 2)

            if tipo == 1:
                tipo = "texto"
            else:
                tipo = "numero"

            columna = {
                "nombre": nombre_variable,
                "tipo": tipo
            }

            tabla["columnas"].append(columna)

        proyecto["tablas"].append(tabla)
        guardar_proyectos(proyectos)

        print("Tabla creada correctamente.")


def mostrar_tablas(proyectos):
    proyecto = elegir_proyecto(proyectos)

    if proyecto != None:
        if len(proyecto["tablas"]) == 0:
            print("El proyecto no tiene tablas.")
        else:
            print("\nTABLAS")

            for i in range(len(proyecto["tablas"])):
                print(i + 1, "-", proyecto["tablas"][i]["nombre"])


def elegir_tabla(proyecto):
    if len(proyecto["tablas"]) == 0:
        print("No hay tablas.")
        return None

    for i in range(len(proyecto["tablas"])):
        print(i + 1, "-", proyecto["tablas"][i]["nombre"])

    opcion = leer_entero("Seleccione una tabla: ", 1, len(proyecto["tablas"]))

    return proyecto["tablas"][opcion - 1]


def agregar_fila(proyectos):
    proyecto = elegir_proyecto(proyectos)

    if proyecto != None:
        tabla = elegir_tabla(proyecto)

        if tabla != None:
            fila = []

            for columna in tabla["columnas"]:
                if columna["tipo"] == "texto":
                    valor = leer_texto("Ingrese " + columna["nombre"] + ": ")
                else:
                    valor = leer_numero("Ingrese " + columna["nombre"] + ": ")

                fila.append(valor)

            tabla["filas"].append(fila)
            guardar_proyectos(proyectos)

            print("Fila agregada correctamente.")


def crear_variable(proyectos):
    proyecto = elegir_proyecto(proyectos)

    if proyecto != None:
        tabla = elegir_tabla(proyecto)

        if tabla != None:
            nombre = leer_texto("Nombre de la nueva variable: ")

            print("1. Texto")
            print("2. Numero")

            tipo = leer_entero("Seleccione el tipo: ", 1, 2)

            if tipo == 1:
                tipo = "texto"
            else:
                tipo = "numero"

            columna = {
                "nombre": nombre,
                "tipo": tipo
            }

            tabla["columnas"].append(columna)

            for fila in tabla["filas"]:
                if tipo == "texto":
                    fila.append("")
                else:
                    fila.append(0.0)

            guardar_proyectos(proyectos)
            print("Variable creada correctamente.")


def mostrar_informacion(proyectos):
    proyecto = elegir_proyecto(proyectos)

    if proyecto != None:
        tabla = elegir_tabla(proyecto)

        if tabla != None:
            print("\n", tabla["nombre"])

            for columna in tabla["columnas"]:
                print(columna["nombre"], end=" | ")

            print()

            for fila in tabla["filas"]:
                for valor in fila:
                    print(valor, end=" | ")

                print()


def modificar_dato(proyectos):
    proyecto = elegir_proyecto(proyectos)

    if proyecto != None:
        tabla = elegir_tabla(proyecto)

        if tabla != None:
            if len(tabla["filas"]) == 0:
                print("No hay filas para modificar.")
            else:
                for i in range(len(tabla["filas"])):
                    print("Fila", i + 1, tabla["filas"][i])

                numero_fila = leer_entero(
                    "Seleccione la fila: ", 1, len(tabla["filas"])
                )

                for i in range(len(tabla["columnas"])):
                    print(i + 1, "-", tabla["columnas"][i]["nombre"])

                numero_columna = leer_entero(
                    "Seleccione la variable: ", 1, len(tabla["columnas"])
                )

                columna = tabla["columnas"][numero_columna - 1]

                if columna["tipo"] == "texto":
                    nuevo_valor = leer_texto("Ingrese el nuevo valor: ")
                else:
                    nuevo_valor = leer_numero("Ingrese el nuevo valor: ")

                tabla["filas"][numero_fila - 1][numero_columna - 1] = nuevo_valor

                guardar_proyectos(proyectos)
                print("Dato modificado correctamente.")


def menu_proyectos(proyectos):
    opcion = 0

    while opcion != 3:
        print("\nMENU PROYECTOS")
        print("1. Crear proyecto")
        print("2. Mostrar proyectos")
        print("3. Volver")

        opcion = leer_entero("Opcion: ", 1, 3)

        if opcion == 1:
            crear_proyecto(proyectos)
        elif opcion == 2:
            mostrar_proyectos(proyectos)


def menu_tablas(proyectos):
    opcion = 0

    while opcion != 4:
        print("\nMENU TABLAS")
        print("1. Crear tabla")
        print("2. Mostrar tablas")
        print("3. Agregar fila")
        print("4. Volver")

        opcion = leer_entero("Opcion: ", 1, 4)

        if opcion == 1:
            crear_tabla(proyectos)
        elif opcion == 2:
            mostrar_tablas(proyectos)
        elif opcion == 3:
            agregar_fila(proyectos)


def menu_variables(proyectos):
    opcion = 0

    while opcion != 3:
        print("\nMENU VARIABLES")
        print("1. Crear variable")
        print("2. Modificar un dato")
        print("3. Volver")

        opcion = leer_entero("Opcion: ", 1, 3)

        if opcion == 1:
            crear_variable(proyectos)
        elif opcion == 2:
            modificar_dato(proyectos)


def menu_principal(proyectos):
    opcion = 0

    while opcion != 6:
        print("\nMENU PRINCIPAL")
        print("1. Proyectos")
        print("2. Tablas")
        print("3. Variables")
        print("4. Mostrar informacion")
        print("5. Estadisticas")
        print("6. Cerrar sesion")

        opcion = leer_entero("Seleccione una opcion: ", 1, 6)

        if opcion == 1:
            menu_proyectos(proyectos)
        elif opcion == 2:
            menu_tablas(proyectos)
        elif opcion == 3:
            menu_variables(proyectos)
        elif opcion == 4:
            mostrar_informacion(proyectos)
        elif opcion == 5:
            seleccionar_datos(proyectos)


def programa_principal():
    usuarios = cargar_usuarios()
    proyectos = cargar_proyectos()

    opcion = 0

    while opcion != 3:
        print("\nMENU DE INGRESO")
        print("1. Registrarse")
        print("2. Iniciar sesion")
        print("3. Salir")

        opcion = leer_entero("Seleccione una opcion: ", 1, 3)

        if opcion == 1:
            registrar_usuario(usuarios)
        elif opcion == 2:
            if iniciar_sesion(usuarios):
                menu_principal(proyectos)

    print("Gracias por utilizar el programa.")


programa_principal()