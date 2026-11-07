from funciones import ordenar_lista, aplicar_operacion

def promedio(datos):
    suma = 0

    for numero in datos:
        suma = suma + numero

    return suma / len(datos)


def calcular_maximo(datos):
    mayor = datos[0]

    for numero in datos:
        if numero > mayor:
            mayor = numero

    return mayor


def calcular_minimo(datos):
    menor = datos[0]

    for numero in datos:
        if numero < menor:
            menor = numero

    return menor


def calcular_mediana(datos):
    datos_ordenados = ordenar_lista(datos.copy())
    cantidad = len(datos_ordenados)
    medio = cantidad // 2

    if cantidad % 2 == 0:
        return (datos_ordenados[medio - 1] +
                datos_ordenados[medio]) / 2
    else:
        return datos_ordenados[medio]


def calcular_varianza(datos):
    media = promedio(datos)
    suma = 0

    for numero in datos:
        suma = suma + (numero - media) ** 2

    return suma / len(datos)


def calcular_frecuencias(datos):
    frecuencias = {}

    for numero in datos:
        if numero in frecuencias:
            frecuencias[numero] = frecuencias[numero] + 1
        else:
            frecuencias[numero] = 1

    return frecuencias


def mostrar_estadisticas(datos):
    print("\nESTADISTICAS")

    print("Cantidad de datos:", len(datos))
    print("Promedio:", aplicar_operacion(datos, promedio))
    print("Maximo:", aplicar_operacion(datos, calcular_maximo))
    print("Minimo:", aplicar_operacion(datos, calcular_minimo))
    print("Mediana:", calcular_mediana(datos))
    print("Varianza:", calcular_varianza(datos))

    print("\nFrecuencias:")
    frecuencias = calcular_frecuencias(datos)

    for numero in frecuencias:
        print(numero, "aparece", frecuencias[numero], "veces")


def seleccionar_datos(proyectos):
    if len(proyectos) == 0:
        print("No hay proyectos cargados.")
        return

    for i in range(len(proyectos)):
        print(i + 1, "-", proyectos[i]["nombre"])

    opcion = leer_opcion(len(proyectos))
    proyecto = proyectos[opcion - 1]

    if len(proyecto["tablas"]) == 0:
        print("Este proyecto no tiene tablas.")
        return

    for i in range(len(proyecto["tablas"])):
        print(i + 1, "-", proyecto["tablas"][i]["nombre"])

    opcion = leer_opcion(len(proyecto["tablas"]))
    tabla = proyecto["tablas"][opcion - 1]

    columnas_numericas = []

    for i in range(len(tabla["columnas"])):
        if tabla["columnas"][i]["tipo"] == "numero":
            columnas_numericas.append(i)

    if len(columnas_numericas) == 0:
        print("La tabla no tiene columnas numericas.")
        return

    print("Columnas numericas:")

    for i in range(len(columnas_numericas)):
        posicion = columnas_numericas[i]
        print(i + 1, "-", tabla["columnas"][posicion]["nombre"])

    opcion = leer_opcion(len(columnas_numericas))
    posicion = columnas_numericas[opcion - 1]

    datos = []

    for fila in tabla["filas"]:
        datos.append(fila[posicion])

    if len(datos) == 0:
        print("No hay datos para calcular.")
    else:
        mostrar_estadisticas(datos)


def leer_opcion(maximo):
    opcion = input("Seleccione una opcion: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > maximo:
        print("Opcion incorrecta.")
        opcion = input("Seleccione una opcion: ")

    return int(opcion)


from funciones import leer_opcion as leer_opcion