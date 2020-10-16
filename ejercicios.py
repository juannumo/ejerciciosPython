# Ejercicio 1 Area de un triángulo

while True:
    try:
        b = int(input("Ingrese el valor de la Base del triángulo  "))
        h = int(input("Ingrese el valor de la altura del triángulo "))
        area = (b*h)/2
        print("El área del triángulo es ", area)
        break
    except ValueError:
        print("Por favor ingrese solo números")
    
# Ejercicio 2 convertir dólares en pesos

while True:
    try:
        dolarInput = float(input("Ingrese la cantidad de dólares que le interesa convertir a pesos colombianos  "))
        valorDolar = 3850
        total = dolarInput * valorDolar
        print("En pesos colombianos se tienen ", total)
        break
    except ValueError:
        print("Por favor ingrese solo números")

    
# Ejercicio 3 Convertir en grados centígrados a grados fahrenheit

while True:
    try:
        centigradoInput = float(input("Ingrese el valor en Grados Centígrados "))
        fah = (centigradoInput * (9/5)) + 32        
        print("En grados Fahrenheit la equivalencia es ", fah)
        break
    except ValueError:
        print("Por favor ingrese solo números")


# Ejercicio 4 Cantidad de segundos de un lustro

lustro = 5 * 365 * 24 * 60 * 60
print("Un lustro tiene ", lustro, " segundos")


# Ejercicio 5 Cantidad de segundos que le toma a la luz desde el Sol hasta Marte

velLuz = 300000
distancia = 227388762
segundos = distancia/velLuz
print("Le toma ", segundos, " segundos a la luz en viajar desde el Sol a Marte")


# Ejercicio 6 Número de vueltas que da una llanta en un Km con diametro de 50cm

import math
pi = math.pi
diametro = 50
radio = diametro/2
perimetro = 2 * pi * radio
vueltas = int(100000 / perimetro)
print("Una llanta de 50cm de diámetro da ", vueltas, " vueltas en Un Kilómetro")

# Ejercicio 7  Longitud de la sombra de un edificio de 20m de altura  cuando el ángulo de los rayos de sol con el suelo son de 22º

# tang alfa = cateto opuesto (altura) / cateto adyacente (Sombra)

import math
catOpuesto = 20
alfaDeg = 22
alfaRad = math.radians(alfaDeg)
catAdy = catOpuesto / math.tan(alfaRad)
print("La longitud de la sombra de un edificio de 20m de altura es ", catAdy, " metros")

# Ejercicio 8 Mostrar True o False

while True:
    try:
        user1 = int(input("Ingrese la edad del usuario 1 "))
        user2 = int(input("Ingrese la edad del usuario 2 "))
        if user1 == user2:
            print("True ")
        else:
            print("False ")
        break
    except ValueError:
        print("Por favor ingrese solo números")

# Ejercicio 9 Meses transcurridos desde la fecha de nacimiento

import datetime
from datetime import timedelta

while True:
    try:
        fecha = input("Ingrese la fecha de nacimiento con el formato DD/MM/YYYY ")
        fecha = datetime.datetime.strptime(fecha,"%d/%m/%Y")
        today = datetime.date.today()
        hoy = datetime.datetime.now()
        difer = hoy - fecha
        break
    except ValueError:
        print("El formato debe ser DD/MM/YYYY")

print ("Los meses transcurridos desde su nacimiento son ", int(difer.days / 30))

# Ejercicio 10 Promedio de alumno que ha cursado 5 materias

while True:
    try:
        espanol = float(input("Ingrese la nota de Español "))
        matematicas = float(input("Ingrese la nota de Matemáticas "))
        economia = float(input("Ingrese la nota de Economía "))
        programacion = float(input("Ingrese la nota de Programación "))
        ingles = float(input("Ingrese la nota de Inglés "))
        promedio = (espanol + matematicas + economia + programacion + ingles)/5
        print("El promedio del alumno es ", promedio)
        break
    except ValueError:
        print("Ingrese solo números")

