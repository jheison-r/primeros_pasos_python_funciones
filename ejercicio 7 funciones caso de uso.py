def leer_ventas():
    ventas = float(input("Digite el monto de ventas del vendedor: "))
    return ventas


def verificar_metas():
    meta = 5000
    total_vendedores = 0
    cumplidos = 0
    mensajes = ""

    while True:
        ventas = leer_ventas()

        if ventas <= 0:
            break

        total_vendedores += 1

        if ventas >= meta:
            cumplidos += 1
            mensajes += "Vendedor " + str(total_vendedores) + ": Meta cumplida\n"

    return total_vendedores, cumplidos, mensajes


def mostrar_resultado(total, cumplidos, mensajes):
    print("\nRESULTADO DE VENTAS")
    print(mensajes)
    print("Total vendedores:", total)
    print("Con meta cumplida:", cumplidos)


# *********** zona de código principal ***********

total, cumplidos, mensajes = verificar_metas()
mostrar_resultado(total, cumplidos, mensajes)