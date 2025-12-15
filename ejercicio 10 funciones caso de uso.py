def leer_horas():
    horas = int(input("Digite horas extra trabajadas: "))
    return horas


def calcular_bonificaciones():
    total_bonificacion = 0
    empleados_bonificados = 0

    while True:
        horas = leer_horas()

        if horas < 0:
            break

        if horas > 0:
            empleados_bonificados += 1

            if horas > 5:
                total_bonificacion += horas * 15
            else:
                total_bonificacion += horas * 10

    return total_bonificacion, empleados_bonificados


def mostrar_resultado(total, empleados):
    print("Total bonificación pagada:", total)
    print("Empleados bonificados:", empleados)


# *********** zona de código principal ***********

total, empleados = calcular_bonificaciones()
mostrar_resultado(total, empleados)