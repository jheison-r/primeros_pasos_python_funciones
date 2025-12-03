#**************zona de funcion**************

def solicitar_precio_producto():
    precio=float(input("Ingrese el precio del producto: "))
    return precio
def definir_descuento():
    descuento=0.1
    return descuento
def calcular_precio_final(precio,descuento):
    precio_descuento=(precio*descuento)
    precio_final=(precio-precio_descuento)
    return precio_final
def imprimir_resultado(resultado_precio):
    print("El precio final con descuento es de: "+str(resultado_precio))

#*************zona de codigo principal**************

precio=solicitar_precio_producto()
descuento=definir_descuento()
precio_final=calcular_precio_final(precio, descuento)
resultado=imprimir_resultado(precio_final)