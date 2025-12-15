def obtener_venta():
    venta = int(input("Digite la cantidad vendida del día: "))
    return venta


def controlar_inventario():
    stock = 50
    punto_reposicion = 10
    mensaje = ""

    while True:
        venta = obtener_venta()
        stock -= venta

        if stock <= punto_reposicion:
            mensaje = "Aviso de Reposición Urgente"
            break

    return stock, mensaje


def mostrar_estado(stock, mensaje):
    print("Stock final:", stock)
    print(mensaje)


# *********** zona de código principal ***********

stock_final, mensaje = controlar_inventario()
mostrar_estado(stock_final, mensaje)