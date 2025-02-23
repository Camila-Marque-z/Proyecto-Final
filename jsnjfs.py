def nombre():
    return input("Ingresa tu nombre: ")

def hora_de_entrada():
    entrada = input("Escribe tu hora de entrada (formato HH:MM AM/PM): ")
    return datetime.datetime.strptime(entrada, '%I:%M %p')

def hora_de_salida():
    salida = input("Escribe tu hora de salida (formato HH:MM AM/PM): ")
    return datetime.datetime.strptime(salida, '%I:%M %p')

def horas_trabajadas(entrada, salida):
    horas = (salida - entrada).total_seconds() / 3600
    print(f"Tus horas trabajadas son: {horas:.2f}")
    return horas

def pago_total(horas, pago):
    total = horas * pago
    print(f"Tu pago total es de: ${total:.2f}")

def salida():
    print("SALISTE")

import datetime

while True:
    print("\nBienvenido")  
 
    print("\n¿Que deseas realizar?")
 
    print("\nIngresa tu hora utilizando hora estandar AM y PM ")

    print("\nEscribe 1 para registrar tu entrada.\nEscribe 2 para registrar tu salida.""\nEscribe 3 para ver tus horas trabajadas.""\nEscribe 4 para ver de cuanto es tu pago total por tus horas trabajadas.\nEscribe 5 para salir. ")

    opcion = int(input("Escribe una opcion: "))

    if opcion == 1:
        nombre_empleado = nombre()
        entrada = hora_de_entrada()
        print(f"{nombre_empleado}, entraste a las {entrada.strftime('%I:%M %p')}")
    elif opcion == 2:
        salida = hora_de_salida()
        print(f"Saliste a las {salida.strftime('%I:%M %p')}")
    elif opcion == 3:
        entrada = hora_de_entrada()
        salida = hora_de_salida()
        horas = horas_trabajadas(entrada, salida)
    elif opcion == 4:
        entrada = hora_de_entrada()
        salida = hora_de_salida()
        horas = horas_trabajadas(entrada, salida)
        tarifa = float(input("Ingresa tu tarifa por hora: "))
        pago_total(horas, tarifa)
    elif opcion == 5:
        salida()
        break
    else: 
        print("ERROR")