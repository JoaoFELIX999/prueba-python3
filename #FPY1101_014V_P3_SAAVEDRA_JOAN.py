#FPY1101_014V_P3_SAAVEDRA_JOAN.PY
import os
os.system("cls")

class Vehiculo:
    def __init__(self, tipo, patente, marca, precio, fecha_registro, run_dueño, nombre_dueño):
        self.tipo = tipo
        self.patente = patente
        self.marca = marca
        self.precio = precio
        self.fecha_registro = fecha_registro
        self.run_dueño = run_dueño
        self.nombre_dueño = nombre_dueño
        self.emision_contaminantes = None
        self.amotaciones_vigentes = None
        self.multas = []

    def imprimir_certificado(self, tipo_certificado):
        if tipo_certificado == 1:
            certificado = "Emisión de contaminantes"
        elif tipo_certificado == 2:
            certificado = "Amotaciones vigentes"
        elif tipo_certificado == 3:
            certificado = "Multas"
        else:
            return "Certificado no válido"

        print(f"Certificado: {certificado}")
        print(f"Patente del vehículo: {self.patente}")
        print(f"Nombre del dueño: {self.nombre_dueño}")
        print(f"RUN del dueño: {self.run_dueño}")

    def agregar_multa(self, descripcion, monto):
        self.multas.append((descripcion, monto))

    def mostrar_informacion(self):
        print("Información del vehículo:")
        print(f"Tipo: {self.tipo}")
        print(f"Patente: {self.patente}")
        print(f"Marca: {self.marca}")
        print(f"Precio: ${self.precio}")
        print(f"Fecha de registro: {self.fecha_registro}")
        print(f"Dueño:")
        print(f"  Nombre: {self.nombre_dueño}")
        print(f"  RUN: {self.run_dueño}")
        print("Multas:")
        for descripcion, monto in self.multas:
            print(f"  - {descripcion}: ${monto}")

def verificar_patente(patente):
    # Verifica el formato de la patente según la descripción dada
    import re
    patron = re.compile(r'^[bcdfghjklpqrstvwxyz]{3}[0-9]{2}$', re.IGNORECASE)
    return re.match(patron, patente) is not None

def main():
    vehiculos = []

    while True:
        print("\nMenú:")
        print("1. Guardar datos ")
        print("2. Buscar vehículo por patente")
        print("3. Imprimir certificados")
        print("4. Salir")

        opcion = input("Ingrese el número de opción deseada: ")

        if opcion == "1":
            tipo = input("Ingrese el tipo de vehículo (Auto, Camión, Camioneta, Motito): ")
            patente = input("Ingrese la patente del vehículo: ")
            if not verificar_patente(patente):
                print("Patente incorrecta. Formato esperado: 3 consonantes seguidas de 2 números.")
                continue
            marca = input("Ingrese la marca del vehículo: ")
            precio = float(input("Ingrese el precio del vehículo: "))
            if precio <= 5000000:
                print("El precio del vehículo debe ser mayor a $5.000.000.")
                continue
            fecha_registro = input("Ingrese la fecha de registro del vehículo: ")
            run_dueño = input("Ingrese el RUN del dueño: ")
            nombre_dueño = input("Ingrese el nombre del dueño: ")

            vehiculo = Vehiculo(tipo, patente, marca, precio, fecha_registro, run_dueño, nombre_dueño)
            vehiculos.append(vehiculo)
            print("Vehículo guardado exitosamente.")

        elif opcion == "2":
            patente_buscar = input("Ingrese la patente del vehículo a buscar: ")
            encontrado = False
            for vehiculo in vehiculos:
                if vehiculo.patente == patente_buscar:
                    vehiculo.mostrar_informacion()
                    encontrado = True
                    break
            if not encontrado:
                print("Vehículo no encontrado.")

        elif opcion == "3":
            tipo_certificado = int(input("Ingrese el tipo de certificado (1. Emisión de contaminantes, 2. Amotaciones vigentes, 3. Multas): "))
            for vehiculo in vehiculos:
                vehiculo.imprimir_certificado(tipo_certificado)

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 4.")

if __name__ == "__main__":
    main()