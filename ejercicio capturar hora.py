def capturar_nombre():
    nombre_usuario = input("escriba el nombre del cliente")
    return nombre_usuario

def capturar_rol():
    rol_usuario = input("escriba su rol")
    return rol_usuario

def capturar_hora():
    hora = int(input("digite la hora"))        
    if hora > 0 and hora < 12: 
     mensaje_hora("buenos dias, ")
    elif hora >= 12 and hora < 18: 
     mensaje_hora("buenas tardes, ")
    elif hora > 18 and hora <= 24:
     mensaje_hora("buenas noches, ")
    else :
        mensaje_hora("hora incorrecta")     
    
     
            
            
def Hacer_saludo(nombre_usuario, hora, rol_usuario):
      mensaje = "hola " + str((mensaje_hora)) + nombre_usuario + ", rol : " + rol_usuario
      return mensaje

def imprimir_mensaje(mensaje):
        print(mensaje)
        

            
    
    # zona de codigo principal
dato_nombre = capturar_nombre()
dato_rol = capturar_rol()
mensaje_hora = capturar_hora()
dato_mensaje = Hacer_saludo(dato_nombre, mensaje_hora, dato_rol)
imprimir_mensaje(dato_mensaje)
