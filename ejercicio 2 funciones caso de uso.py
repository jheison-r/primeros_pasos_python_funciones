def obtener_codigo():
    codigo = input("Digite el código del empleado (o SALIR para terminar): ")
    return codigo


def validar_acceso(codigo, codigo_especial):
    if codigo == codigo_especial:
        return True
    else:
        return False


def controlar_accesos():
    codigo_especial = "INV-001"
    accesos_permitidos = 0
    accesos_denegados = 0
    mensajes = ""

    while True:
        codigo = obtener_codigo()

        if codigo == "SALIR":
            break

        acceso = validar_acceso(codigo, codigo_especial)

        if acceso == True:
            mensajes += "Acceso permitido al empleado con código " + codigo + "\n"
            accesos_permitidos += 1
        else:
            mensajes += "Acceso denegado al empleado con código " + codigo + "\n"
            accesos_denegados += 1

    return mensajes, accesos_permitidos, accesos_denegados


def mostrar_resultado(mensajes, permitidos, denegados):
    print("\nREGISTRO DE ACCESOS")
    print(mensajes)
    print("Accesos permitidos:", permitidos)
    print("Accesos denegados:", denegados)


# *********** zona de código principal ***********

mensajes, permitidos, denegados = controlar_accesos()
mostrar_resultado(mensajes, permitidos, denegados)