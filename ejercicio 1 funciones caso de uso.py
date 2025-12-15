def cantidad_pedidos():
    pedidos = 30
    return pedidos


def procesar_datos(pedidos):
    suma = 0

    for i in range(pedidos):
        producto = input("Digite el producto: ")

        calificacion = int(input("Digite del 1 al 5 el nivel de satisfacción con el pedido: "))

        if calificacion == 5:
            print("EXCELENTE")

        suma += calificacion  # suma correcta

    return suma


def hacer_calculo(suma, pedidos):
    promedio = suma / pedidos
    return promedio


def imprimir_resultado(promedio):
    print("El promedio de satisfacción es de: " + str(promedio))


# *********** zona de código principal ***********

pedidos = cantidad_pedidos()
suma = procesar_datos(pedidos)
promedio = hacer_calculo(suma, pedidos)
imprimir_resultado(promedio)