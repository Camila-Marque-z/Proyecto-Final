import datetime

def nombre():
    return input("Ingresa tu nombre: ")

def hora_de_entrada():
    a = input("Escribe tu hora de entrada (formato HH:MM AM/PM): ")
    return datetime.datetime.strptime(a, '%I:%M %p')

def hora_de_salida():
    b = input("Escribe tu hora de salida (formato HH:MM AM/PM): ")
    return datetime.datetime.strptime(b, '%I:%M %p')

def horas_trabajadas(a, b):
    horas = (b - a).total_seconds() / 3600
    print(f"Tus horas trabajadas son: {horas:.2f}")
    return horas

def pago_total(horas, pago):
    total = horas * pago
    print(f"Tu pago total es de: ${total:.2f}")

def salida():
    print("SALISTE")

while True:
    print("\nBienvenido")  
    print("\n¿Que deseas realizar?")
    print("\nIngresa tu hora utilizando hora estandar am o pm")
    print("\nEscribe 1 para registrar tu entrada.\nEscribe 2 para registrar tu salida.")
    print("Escribe 3 para ver tus horas trabajadas.")
    print("Escribe 4 para ver de cuanto es tu pago total por tus horas trabajadas.")
    print("Escribe 5 para salir.")

    opcion = int(input("Escribe una opcion: "))

    if opcion == 1:
        empleado = nombre()
        a = hora_de_entrada()
        print(f"{empleado}, entraste a las {a.strftime('%I:%M %p')}")
    elif opcion == 2:
        b = hora_de_salida()
        print(f"Saliste a las {b.strftime('%I:%M %p')}")
    elif opcion == 3:
        a = hora_de_entrada()
        b = hora_de_salida()
        horas = horas_trabajadas(a, b)
    elif opcion == 4:
        a = hora_de_entrada()
        b = hora_de_salida()
        horas = horas_trabajadas(a, b)
        pago = float(input("Ingresa tu pago por hora: "))
        pago_total(horas, pago)
    elif opcion == 5:
        b()
        break
    else: 
        print("ERROR")