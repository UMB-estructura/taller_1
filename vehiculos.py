"""
b) Haciendo uso de estructuras de datos estáticos (vectores y matrices) sin POO, Generar un Algoritmo que guarda una matriz de N vehículos 
(Mazda, Toyota, etc.) con sus respectivos precios durante los últimos 5 años (2019, 2020, 2021 ,2022, 2023), 
los cuales son ingresados por teclado (validar que el valor que se introduce sea positivo, si introduce valores negativos o cero debe mostrar mensaje
que solo se permiten valores positivos y permitirle digitar nuevamente el precio). Mostrar:
•	Mediante una función/método mostrar el promedio de los autos que cuestan entre 30 y 50 millones del año seleccionado por el usuario.
"""

list = {
    19 : {},
    20 : {},
    21 : {},
    22 : {},
    23 : {}
}

def indata(list):
    s = int(input("ingrese el año al que desea ingresar un auto:\t"))
    while s != None:
        if (s >= 19 and s <= 23) or (s >= 2019 and s <= 2023):
            for i in list:
                if s == i:
                    a = input("marca:\t")
                    list[i][a] = int(input("precio:\t"))
                    return list 
        else:
            print("año invalido")
            return list

def pr(list):
    for i in list:
        print("auto:\t" + str(i))
        for a in list[i]:
            print(a + "\t" + str(list[i][a]))

def bara(list):
    for i in list:
        x = 0
        for a in list[i]:
            if x < list[i][a]:
                s = a
                x = list[i][a]
        
        print("año: "+i+"\nel auto mas barato fue: "+s+"\tprecio: "+x)

def prom(list):
    x = {
        19 : {},
        20 : {},
        21 : {},
        22 : {},
        23 : {}
    }
    for i in list:
        for a in list[i]:
            if list[i][a] > 30000000 and list[i][a] < 50000000:
                x[i][a] =  list[i][a]

    print(x)


while True:
    print(
        "lista de opciones\n1) ingresar datos\n2) mostar datos\n3) mostrar los autos más baratos de cada año\n4) el promedio de los autos que cuestan entre 30 y 50 millones"
    )
    s = int(input("ingrese su opcion:\t"))
    if s == 1:
        list = indata(list)
    elif s == 2:
        pr(list)
    elif s == 3:
        bara(list)
    elif s == 4:
        prom(list)
    else:
        print("error, seleccione una opcion valida")