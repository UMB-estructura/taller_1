"""
    Generar sin POO, un programa que por cada día de la semana (lunes a domingo) acumula la cantidad de ventas totales diarias de una empresa,
    la empresa tiene 6 sedes. Mediante funciones llenar la matriz con las ventas respectivas,
    haciendo uso de funciones por cada sede mostrar los días que tienen ventas totales diarias por encima de la media de la semana respectiva y
    el promedio de ventas total de la semana de la empresa y por cada sede. De igual manera generar un procedimiento/método que permita aumentar 
    en un 15% las ventas diarias que estén por debajo de la media respectiva de cada sede.
"""

ventas = {
    "lunes":{
        1:None,
        2:None,
        3:None,
        4:None,
        5:None,
        6:None
        },
    "martes":{
        1:None,
        2:None,
        3:None,
        4:None,
        5:None,
        6:None
        },
    "miercoles":{
        1:None,
        2:None,
        3:None,
        4:None,
        5:None,
        6:None
        },
    "jueves":{
        1:None,
        2:None,
        3:None,
        4:None,
        5:None,
        6:None
        },
    "viernes":{
        1:None,
        2:None,
        3:None,
        4:None,
        5:None,
        6:None
        },
    "sabado":{
        1:None,
        2:None,
        3:None,
        4:None,
        5:None,
        6:None
        },
    "domingo":{
        1:None,
        2:None,
        3:None,
        4:None,
        5:None,
        6:None
        }
}

def main (ventas):
    print("opciones:\n1)ingresar datos\n2)ventas superiores\n3)ventas deseadas")
    s = int(input("->"))
    
    if s == 1:
        ventas = setdata(ventas)
    elif s == 2:
        print(sup(ventas))
    elif s == 3:
        ventas = arre(ventas)
    else:
        print ("opcion incorrecta")

def setdata(ventas):
    t = int(input("ingrese el ID de su tienda:"))
    d = input("ingrese dia: (en minuscula y sin caracteres especiales) ")
    
    if d in ventas:
        if t in ventas[d]:
            ventas[d][t] = float(input("total del dia : "))
            return ventas
        else:
            print("tineda invalida")
            return None
    else:
        print("dia invalido")
        return(ventas)
    
def sup(ventas):
    t = 0
    c = 0
    for i in ventas:
        for a in ventas[i]:
            t += ventas[i][a]
            c += 1
            
    t  = t / c
    c = {}
    for i in ventas:
        for a in ventas[i]:
            if ventas[i][a] >= t:
                c[i][a] = ventas[i][a]
    
    return c

def arre(ventas):
    t = 0
    c = 0
    for i in ventas:
        for a in ventas[i]:
            t += ventas[i][a]
            c += 1
            
    t  = t / c
    
    for i in ventas:
        for a in ventas[i]:
            if ventas[i][a] < t:
                ventas[i][a] = ventas[i][a] + (ventas[i][a] * 0.15)

while True:
    main(ventas)