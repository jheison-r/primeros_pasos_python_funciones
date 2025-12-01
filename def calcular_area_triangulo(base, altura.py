
def definir_base():
     base_triangulo =10

     return base_triangulo

def definir_altura():
     altura_triangulo =7

     return altura_triangulo


def calcular_area(base, altura):
    
    area= (base*altura)/2    
    
    
    return area
    
def imprimir_datos(base_triangulo, altura_triangulo):
    mensaje= "la base es: "+base_triangulo
    mensaje="la altura es: "+altura_triangulo
    

def imprimir_resultado(resultado_area):

 print("El area del triangulo con base es "  + str(resultado_area))
 
 

#*******************zona de codigo principal********************


base= definir_base()
altura= definir_altura()
area= calcular_area(base, altura)
reultado= imprimir_resultado(area)

