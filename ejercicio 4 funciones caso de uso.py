def procesar_lote():
    unidades = int(input("Digite cantidad de unidades del lote: "))
    defectuosas = 0
    registros = ""

    for i in range(unidades):
        estado = input("Unidad defectuosa (D) u OK (O): ")

        if estado == "D":
            defectuosas += 1
            registros += "Fallo en unidad " + str(i + 1) + "\n"
        else:
            registros += "Unidad " + str(i + 1) + " OK\n"

    porcentaje = (defectuosas / unidades) * 100
    return defectuosas, unidades, porcentaje, registros


def control_produccion():
    while True:
        opcion = input("Digite cualquier tecla para continuar o STOP para terminar: ")

        if opcion == "STOP":
            break

        defectuosas, total, porcentaje, registros = procesar_lote()
        print(registros)
        print("Defectuosas:", defectuosas)
        print("Porcentaje defectuoso:", porcentaje, "%")


# *********** zona de código principal ***********

control_produccion()