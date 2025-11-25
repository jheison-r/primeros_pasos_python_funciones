def tomar_mes():
    numero=int(input("digite un numero del 1 al 12: "))
    return numero
def num_corres(num_mes):
    match num_mes:
        case 1:
           return "enero"
        case 2:
           return "febrero"
        case 3:
           return "marzo"
        case 4: 
           return "abril"
        case 5:
           return "mayo"
        case 6:
           return "junio" 
        case 7:
           return "julio" 
        case 8:
           return "agosto"
        case 9:
           return "septiembre"
        case 10:
           return "octubre" 
        case 11:
           return "noviembre"
        case 12:
           return "diciembre"
       
def imprimir_mes(dato_mes):
    print("El nombre de tu mes es: " + str(dato_mes)) 


#codigo principal
num_mes = tomar_mes()
dato_mes = num_corres(num_mes)
imprimir_mes(dato_mes)