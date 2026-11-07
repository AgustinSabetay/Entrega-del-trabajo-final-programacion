import csv

def leer_texto(mensaje):
    texto = input(mensaje)

    while texto == "":
        print("El texto no puede estar vacio.")
        texto = input(mensaje)

    return texto

def es_numero(texto):
    texto = texto.replace(",", ".")
    posicion = 0
    puntos = 0
    digitos = 0

    if texto == "":
        return False

    if texto[0] == "-":
        posicion = 1

    if posicion == len(texto):
        return False

    while posicion < len(texto):
        if texto[posicion] == ".":
            puntos = puntos + 1
        elif texto[posicion].isdigit():
            digitos = digitos + 1
        else:
            return False

        posicion = posicion + 1

    if puntos > 1 or digitos == 0:
        return False

    return True


def leer_numero(mensaje):
    texto = input(mensaje)

    while not es_numero(texto):
        print("Ingrese un numero valido.")
        texto = input(mensaje)

    texto = texto.replace(",", ".")
    return float(texto)


def leer_entero(mensaje, minimo, maximo):
    texto = input(mensaje)

    while not texto.isdigit() or int(texto) < minimo or int(texto) > maximo:
        print("Ingrese una opcion valida.")
        texto = input(mensaje)

    return int(texto)


def ordenar_burbuja(lista):
    i = 0

    while i < len(lista):
        j = 0

        while j < len(lista) - 1:
            if lista[j] > lista[j + 1]:
                auxiliar = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = auxiliar

            j = j + 1

        i = i + 1

    return lista


def mostrar_recursivo(lista, posicion=0):
    if posicion < len(lista):
        print(lista[posicion])
        mostrar_recursivo(lista, posicion + 1)


def aplicar_operacion(datos, funcion):
    return funcion(datos)


def guardar_usuarios(usuarios):
    archivo = open("usuarios.txt", "w")

    for usuario in usuarios:
        archivo.write(usuario["nombre"] + "|" + usuario["clave"] + "\n")

    archivo.close()


def cargar_usuarios():
    usuarios = []

    archivo = open("usuarios.txt", "a")
    archivo.close()

    archivo = open("usuarios.txt", "r")
    lineas = archivo.readlines()
    archivo.close()

    for linea in lineas:
        datos = linea.strip().split("|")

        if len(datos) == 2:
            usuario = {
                "nombre": datos[0],
                "clave": datos[1]
            }

            usuarios.append(usuario)

    return usuarios


def guardar_proyectos(proyectos):
    archivo = open("proyectos.csv", "w", newline="")
    escritor = csv.writer(archivo)

    for proyecto in proyectos:
        escritor.writerow(["P", proyecto["nombre"]])

        for tabla in proyecto["tablas"]:
            escritor.writerow(["T", proyecto["nombre"], tabla["nombre"]])

            for columna in tabla["columnas"]:
                escritor.writerow([
                    "C",
                    proyecto["nombre"],
                    tabla["nombre"],
                    columna["nombre"],
                    columna["tipo"]
                ])

            for fila in tabla["filas"]:
                escritor.writerow(
                    ["R", proyecto["nombre"], tabla["nombre"]] + fila
                )

    archivo.close()


def cargar_proyectos():
    proyectos = []

    archivo = open("proyectos.csv", "a", newline="")
    archivo.close()

    archivo = open("proyectos.csv", "r", newline="")
    lector = csv.reader(archivo)

    for datos in lector:
        if len(datos) > 0:

            if datos[0] == "P":
                proyecto = {
                    "nombre": datos[1],
                    "tablas": []
                }

                proyectos.append(proyecto)

            elif datos[0] == "T":
                proyecto = buscar_proyecto(proyectos, datos[1])

                if proyecto != None:
                    tabla = {
                        "nombre": datos[2],
                        "columnas": [],
                        "filas": []
                    }

                    proyecto["tablas"].append(tabla)

            elif datos[0] == "C":
                tabla = buscar_tabla(proyectos, datos[1], datos[2])

                if tabla != None:
                    columna = {
                        "nombre": datos[3],
                        "tipo": datos[4]
                    }

                    tabla["columnas"].append(columna)

            elif datos[0] == "R":
                tabla = buscar_tabla(proyectos, datos[1], datos[2])

                if tabla != None:
                    fila = []

                    for i in range(3, len(datos)):
                        posicion = i - 3

                        if tabla["columnas"][posicion]["tipo"] == "numero":
                            fila.append(float(datos[i]))
                        else:
                            fila.append(datos[i])

                    tabla["filas"].append(fila)

    archivo.close()

    return proyectos


def buscar_proyecto(proyectos, nombre):
    for proyecto in proyectos:
        if proyecto["nombre"] == nombre:
            return proyecto

    return None


def buscar_tabla(proyectos, nombre_proyecto, nombre_tabla):
    proyecto = buscar_proyecto(proyectos, nombre_proyecto)

    if proyecto != None:
        for tabla in proyecto["tablas"]:
            if tabla["nombre"] == nombre_tabla:
                return tabla

    return None


def exportar_csv(tabla):
    nombre_archivo = leer_texto("Nombre del archivo CSV: ")

    if not nombre_archivo.endswith(".csv"):
        nombre_archivo = nombre_archivo + ".csv"

    archivo = open(nombre_archivo, "w", newline="")
    escritor = csv.writer(archivo)

    encabezados = []

    for columna in tabla["columnas"]:
        encabezados.append(columna["nombre"])

    escritor.writerow(encabezados)

    for fila in tabla["filas"]:
        escritor.writerow(fila)

    archivo.close()

    print("Archivo exportado correctamente.")


def importar_csv(tabla):
    nombre_archivo = leer_texto("Nombre del archivo CSV: ")

    if not nombre_archivo.endswith(".csv"):
        nombre_archivo = nombre_archivo + ".csv"

    archivo = open(nombre_archivo, "r", newline="")
    lector = csv.reader(archivo)

    encabezados = next(lector, [])

    nombres_columnas = []

    for columna in tabla["columnas"]:
        nombres_columnas.append(columna["nombre"])

    if encabezados == nombres_columnas:
        filas_nuevas = []

        for datos in lector:
            if len(datos) == len(tabla["columnas"]):
                fila = []
                valido = True

                for i in range(len(datos)):
                    if tabla["columnas"][i]["tipo"] == "numero":
                        if es_numero(datos[i]):
                            fila.append(float(datos[i]))
                        else:
                            valido = False
                    else:
                        fila.append(datos[i])

                if valido:
                    filas_nuevas.append(fila)

        tabla["filas"].extend(filas_nuevas)
        print("Archivo importado correctamente.")
    else:
        print("Las columnas del archivo no coinciden con la tabla.")

    archivo.close()