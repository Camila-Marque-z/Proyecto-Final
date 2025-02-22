def hora_de_entrada(a):
    print(f"Tu entraste a las:", a)
def hora_de_salida(b):
    print(f"Tu saliste a las:", b)
def horas_trabajadas(b, a):
    print(f"Tus horas trabajadas son:{b - a}")
def pago_total(a,b,z):
    print(f"Tu pago total es de:{(b - a) * -z}")
def salida():
    print("SALISTE")


while True:
    print("\nBienvenido")  
 
    print("\n¿Que deseas realizar?")
 
    print("\nEscribe 1 para registrar tu entrada.\nEscribe 2 para registrar tu salida.\nEscribe 3 para ver tus horas trabajadas.\nEscribe 4 para ver de cuanto es tu pago total por tus horas trabajadas.\nEscribe 5 para salir. ")

    
    opcion = int(input("Esribe una opcion: "))


    if opcion == 1:
        a = int(input("Escribe tu hora de entrada: "))
        hora_de_entrada(a)
    elif opcion == 2:
        b = int(input("Escribe tu hora de salida: "))
        hora_de_salida(b)
    elif opcion == 3:
        a = int(input("Escribe tu hora de entrada: "))
        b = int(input("Escribe tu hora de salida: "))
        horas_trabajadas(b, a)
    elif opcion == 4:
        a = int(input("Escribe tu hora de entrada: "))
        b = int(input("Escribe tu hora de salida: "))
        z = 4.00
        pago_total( b, a, z)
    elif opcion == 5:
        salida()
        break
    else: 
        print("ERROR")

    