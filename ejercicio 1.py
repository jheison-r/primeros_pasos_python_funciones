# zona de funciones 
# 1. crear datos
def tomar_nombre():
    nombre_cliente = input("digite el nombre del usurio: ")
    return nombre_cliente 

# 2. procesar datos o informacion 
def hacer_mensaje(nombre_cliente):
    mensaje = nombre_cliente + "hola..."
    return mensaje 

# 3. mostrar resultados (mensaje)
def imprimir_info(mensaje):
    print("hola mundo de python")
    print(mensaje)


# zonade codigo principal

# tomar datos del cliente omar

nombre_cliente = tomar_nombre() # aqui van argumento