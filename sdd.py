import datetime

# Lista para almacenar los registros de entrada y salida
registros = []

# Función para registrar entrada/salida
def registrar_entrada_salida():
    nombre = input("Ingrese el nombre del empleado: ")
    tipo = input("¿Es una entrada o salida? (E/S): ").upper()
    tiempo = datetime.datetime.now()
    registros.append((nombre, tipo, tiempo))
    print(f"Registro de {tipo} para {nombre} a las {tiempo.strftime('%Y-%m-%d %I:%M %p')}")

# Función para calcular el pago total
def calcular_pago_total(tarifa_por_hora):
    pagos = {}
    for nombre, tipo, tiempo in registros:
        if tipo == 'E':
            if nombre not in pagos:
                pagos[nombre] = {'entrada': tiempo, 'total_horas': 0}
            else:
                pagos[nombre]['entrada'] = tiempo
        elif tipo == 'S' and nombre in pagos and 'entrada' in pagos[nombre]:
            horas_trabajadas = (tiempo - pagos[nombre]['entrada']).total_seconds() / 3600
            pagos[nombre]['total_horas'] += horas_trabajadas
            del pagos[nombre]['entrada']
    
    for nombre, datos in pagos.items():
        total_pago = datos['total_horas'] * tarifa_por_hora
        print(f"Empleado: {nombre}, Horas trabajadas: {datos['total_horas']:.2f}, Pago total: ${total_pago:.2f}")

# Función para ver el historial
def ver_historial():
    for nombre, tipo, tiempo in registros:
        print(f"Empleado: {nombre}, Tipo: {tipo}, Tiempo: {tiempo.strftime('%Y-%m-%d %I:%M %p')}")

# Menú principal
def menu():
    while True:
        print("\nMenú:")
        print("1. Registrar entrada/salida")
        print("2. Calcular pago total")
        print("3. Ver historial")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_entrada_salida()
        elif opcion == '2':
            tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))
            calcular_pago_total(tarifa_por_hora)
        elif opcion == '3':
            ver_historial()
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()