def leer_uso_cpu():
    uso = float(input("Digite el uso de CPU (%): "))
    return uso


def monitorear_cpu():
    total_mediciones = 0
    alertas_criticas = 0
    mensajes = ""

    while True:
        uso = leer_uso_cpu()

        if uso < 0:
            break

        total_mediciones += 1

        if uso > 90:
            mensajes += "Alerta: Uso Crítico (" + str(uso) + "%)\n"
            alertas_criticas += 1

    return total_mediciones, alertas_criticas, mensajes


def mostrar_reporte(total, alertas, mensajes):
    print("\nREPORTE DE CPU")
    print(mensajes)
    print("Total de mediciones:", total)
    print("Alertas críticas:", alertas)


# *********** zona de código principal ***********

total, alertas, mensajes = monitorear_cpu()
mostrar_reporte(total, alertas, mensajes)