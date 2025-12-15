def leer_edad():
    edad = int(input("Digite la edad del participante: "))
    return edad


def procesar_encuesta():
    total_personas = 0
    publico_objetivo = 0
    suma_edades = 0
    mensajes = ""

    while True:
        edad = leer_edad()

        if edad == 0:
            break

        total_personas += 1
        suma_edades += edad

        if edad >= 25 and edad <= 45:
            publico_objetivo += 1
            mensajes += "Edad dentro del rango: " + str(edad) + "\n"

    promedio = 0
    if total_personas > 0:
        promedio = suma_edades / total_personas

    return total_personas, publico_objetivo, promedio, mensajes


def mostrar_reporte(total, objetivo, promedio, mensajes):
    print("\nREPORTE DE ENCUESTA")
    print(mensajes)
    print("Total participantes:", total)
    print("Público objetivo:", objetivo)
    print("Edad promedio:", promedio)


# *********** zona de código principal ***********

total, objetivo, promedio, mensajes = procesar_encuesta()
mostrar_reporte(total, objetivo, promedio, mensajes)