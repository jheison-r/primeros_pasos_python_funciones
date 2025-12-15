def ingresar_productos():
    subtotal = 0

    while True:
        precio = input("Digite precio del producto o FIN para terminar: ")

        if precio == "FIN":
            break

        precio = float(precio)
        cantidad = int(input("Digite cantidad: "))

        subtotal += precio * cantidad

    return subtotal


def calcular_descuento(subtotal):
    descuento = 0
    mensaje = "No se aplicó descuento"

    if subtotal > 1000:
        descuento = subtotal * 0.10
        mensaje = "Descuento aplicado del 10%"
    elif subtotal > 500:
        descuento = subtotal * 0.05
        mensaje = "Descuento aplicado del 5%"

    total = subtotal - descuento
    return total, mensaje


def mostrar_factura(total, mensaje):
    print(mensaje)
    print("Total a pagar:", total)


# *********** zona de código principal ***********

subtotal = ingresar_productos()
total, mensaje = calcular_descuento(subtotal)
mostrar_factura(total, mensaje)