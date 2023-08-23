from colorama import Fore
from funciones import *

def opcionesMenu():
    print(Fore.MAGENTA +"\n    --------------------- MENÚ --------------------")
    print(Fore.MAGENTA +"   |     1. Cargar inventario inicial              |")
    print(Fore.MAGENTA +"   |     2. Cargar instrucciones de movimientos    |")
    print(Fore.MAGENTA +"   |     3. Crear informe de inventario            |")
    print(Fore.MAGENTA +"   |     4. Salir                                  |")
    print(Fore.MAGENTA +"    ---------------------------------------------- ")

def menu():
    opcion = ""

    while opcion != "4":
        opcionesMenu()
        opcion = input(Fore.WHITE +"Seleccione una opción del Menu: ")

        if opcion == "1":
            cargarArchivoINV()
        elif opcion == "2":
            cargarArchivoMOV()
        elif opcion == "3":
            crearInformeInventario()
        elif opcion == "4":
            print(Fore.WHITE +"     Hasta pronto!")
            break
               
if __name__ == "__main__":
    menu()