import datetime

def hora_de_entrada():
    a = input("Escribe tu hora de entrada: ")
    return datetime.datetime.strptime(a, '%I:%M %p')
def hora_de_salida():
    b = input("Escribe tu hora de salida: ")
    return datetime.datetime.strptime(b, '%I:%M %p')
def horas_trabajadas():
    print(f"Tus horas trabajadas son:{b - a}")
def pago_total(horas, pago):
    total = horas * pago
    print(f"Tu pago total es:  ${total:.2f}")
def salida():
    print("SALISTE")

while True:
    print("\nBienvenido")  
 
    print("\n¿Que deseas realizar?")
 
    print("\nIngresa tu hora utilizando hora estandar: Hora:Minutos AM o PM")

    print("\nEscribe 1 para registrar tu entrada.\nEscribe 2 para registrar tu salida.""\nEscribe 3 para ver tus horas trabajadas.""\nEscribe 4 para ver de cuanto es tu pago total por tus horas trabajadas.\nEscribe 5 para salir. ")

    
    opcion = int(input("Esribe una opcion: "))


    if opcion == 1 :
        a = hora_de_entrada() 
        print(f"Tu entraste a las {a.strftime('%I:%M %p')}")
    elif opcion == 2 :
        b = hora_de_salida() 
        print(f"Saliste a las {b.strftime('%I:%M %p')}")
    elif opcion == 3:
        a = hora_de_entrada()
        b = hora_de_salida()
        horas_trabajadas()
    elif opcion == 4:
        a = hora_de_entrada()
        b = hora_de_salida()
        horas = horas_trabajadas()
        pago = float(input("Ingresa tu pago por hora: "))
        total = horas * pago
        pago_total(horas, pago)
    elif opcion == 5:
        salida()
        break
    else: 
        print("ERROR")

    