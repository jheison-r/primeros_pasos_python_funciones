def capturar_numero():
 numero = int(input("digite un numero"))
 return numero
def validar_numero(dato_numero):
  if dato_numero > 0:
    mensaje= "el numero es positivo"
  elif dato_numero ==0:
    mensaje="el numero es neutro" 
  else:
    mensaje="el numero es negativo"
    return mensaje

def imprimir_numero(dato_mensaje):
 print("el numero es: " + str(dato_mensaje))

#codigo principal
dato_numero = capturar_numero()
dato_mensaje = validar_numero(dato_numero)
imprimir_numero(dato_mensaje)





