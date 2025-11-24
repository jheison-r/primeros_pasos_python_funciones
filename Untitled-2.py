

def capturar_nombre():
    nombre_usuario = input("escriba el nombre del cliente")
    return nombre_usuario

def capturar_rol():
    rol_usuario = input("escriba su rol")
    return rol_usuario

def Hacer_saludo(nombre_usuario, rol_usuario):
    mensaje = "hola " + nombre_usuario + ", rol : " + rol_usuario
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje) 
    

# zona de codigo principal
dato_nombre = capturar_nombre()
dato_rol = capturar_rol()
dato_mensaje = Hacer_saludo(dato_nombre, dato_rol)
imprimir_mensaje(dato_mensaje)