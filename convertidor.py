##CONVERTIDOR DE CSV A PDF
import csv
import os
import csv
import os

def limpiar():
    os.system('cls')

##CALCULAR GANANCIAS

def ganancias():
    cunit = 10
    preciov=20
    cantidad=2
    ganancia = (preciov - cunit) * cantidad
    print(ganancia)
    
ganancias()


def convertir():
    with open('ventas.csv') as File:
        reader = csv.DictReader(File)
        for row in reader:
            print(row)
            print(row['id'], row['fecha'], row['producto'], row['cantidad'], row['precio'], row['costo'], row['ganancia'])

def menu():
    limpiar()
    print('''
    1. Convertir CSV a PDF
    2. Ganancias
    3. Salir
    ''')
    opcion = input('Ingrese una opcion: ')
    if opcion == '1':
        convertir()
    elif opcion == '2':
        ganancias()
    elif opcion == '3':
        exit()
    else:
        print('Opcion no valida')
    input('Presione una tecla para continuar')
    menu()

