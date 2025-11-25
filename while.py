def capturar_letra():
    while True:
        print("digite la letra 'A'  para actualizar sistema")
        print("digite la letra 'E'  para eliminar catalogo")
        print("digite la letra 'C'  para crear productos")
        print("digite la letra 'S'  para salir del programa")
        letra=str(input("seleccione una opcion..."))
        return letra


def validar_letra(dato_letra):
    if dato_letra =='S' or dato_letra =='s':
        mensaje = "saliemdo del sisitema..."
        
    elif dato_letra == 'A' or dato_letra=='s':
        mensaje = "actualizando el sistema..."
    elif dato_letra== 'E' or dato_letra=='e':
        mensaje = "eliminando catalogo..."
    elif dato_letra== 'C' or dato_letra== 'c':
        mensaje= "creando productos..."
    

    return mensaje


def imprimir_mensaje(dato_mensaje):
    print("usted esta " + dato_mensaje)

#codigo principal

dato_letra= capturar_letra()
dato_mensaje= validar_letra(dato_letra)
imprimir_mensaje(dato_mensaje)





    