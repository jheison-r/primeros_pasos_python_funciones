def definir_largo():
     largo =40

     return largo

def definir_ancho():
     ancho =60

     return ancho


def calcular_area(largo, ancho):
    
    area= (largo*ancho)/2    
    
    
    return area
    
def imprimir_datos(largo, ancho):
    mensaje= "la base es: "+largo
    mensaje="la altura es: "+ancho
    

def imprimir_resultado(resultado_area):

 print("El area del rectangulo  es "  + str(resultado_area))
 
 

#*******************zona de codigo principal********************


largo= definir_largo()
ancho= definir_ancho()
area= calcular_area(largo, ancho)
reultado= imprimir_resultado(area)