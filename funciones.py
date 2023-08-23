from colorama import Fore

def cargarProducto(productos): #funcion cargar producto, retorna lista de inventario
    listaCrearProducto = []
    for lineaInv in productos.readlines():
        datos = lineaInv.split(" ")
        datos2 = datos[1].split(";")
        datoConSaltoDeLinea = datos2[-1]
        if datos[0].startswith("crear_producto"):
            listaCrearProducto.append((datos2[0], datos2[1], datos2[2], datoConSaltoDeLinea.strip("\n")))
    #print(listaCrearProducto)
    productos.close()
    return listaCrearProducto

def agregarProducto(productos): #funcion agregar producto, retorna lista de movimientos "Agregar"
    listaAgregarStock = []
    for lineaMov in productos.readlines():
        datos = lineaMov.split(" ")
        datos2 = datos[1].split(";")
        datoConSaltoDeLinea = datos2[-1]
        if datos[0].startswith("agregar_stock"):
            listaAgregarStock.append((datos2[0], datos2[1], datoConSaltoDeLinea.strip("\n")))
    productos.close()
    return listaAgregarStock

def venderProducto(productos): #funcion vender producto, retorna lista de movimientos "Vender"
    listaVenderProducto = []
    for lineaMov in productos.readlines():
        datos = lineaMov.split(" ")
        datos2 = datos[1].split(";")
        datoConSaltoDeLinea = datos2[-1]
        if datos[0].startswith("vender_producto"):
            listaVenderProducto.append((datos2[0], datos2[1], datoConSaltoDeLinea.strip("\n")))
    productos.close()
    return listaVenderProducto

#rutas predeterminadas
rutaINV = ("inventario.inv")
cargarINV = cargarProducto(open(rutaINV, "r", encoding="utf-8"))

rutaMOV = ("movimientos.mov")
cargarMOVtalqueAgrega = agregarProducto(open(rutaMOV, "r", encoding="utf-8"))
cargarMOVtalqueVende = venderProducto(open(rutaMOV, "r", encoding="utf-8"))


def crearInforme():
    cargarINV
    cargarMOVtalqueAgrega
    cargarMOVtalqueVende
    listaProcesarDatos = []
    for producto in cargarINV:
        nombres = producto[0]
        cantidades = producto[1]
        precios = producto[2]
        ubicaciones = producto[3]
        for agregar in cargarMOVtalqueAgrega:
            nombres2 = agregar[0]
            cantidades2 = agregar[1]
            ubicaciones2 = agregar[2]
            for cargarMOVtalqueAgrega, (nombres, cantidades, precios, ubicaciones) in enumerate(cargarINV):
                if nombres==ubicaciones:
                    if nombres==nombres2 and ubicaciones==ubicaciones2:
                        actual = int(cantidades)
                        agregado = int(cantidades2)
                        nuevoValor = actual + agregado
                        listaProcesarDatos.append(nombres, nuevoValor, precios, ubicaciones)
                    else:
                        print(Fore.RED +"No se han podido agregar Productos")
                for vender in cargarMOVtalqueVende:
                    nombres3 = vender[0]
                    cantidades3 = vender[1]
                    ubicaciones3 = vender[2]
                    for cargarMOVtalqueVende, (nombres, cantidades, precios, ubicaciones) in enumerate(cargarINV):
                        if nombres==ubicaciones:
                            if nombres==nombres3 and ubicaciones==ubicaciones3:
                                actual = int(cantidades)
                                vendido = int(cantidades3)
                                nuevoValor2 = actual - vendido
                                if vendido < actual:
                                    listaProcesarDatos.append(nombres, nuevoValor2 , precios, ubicaciones)
                            else:
                                print(Fore.RED +"No se han podido agregar Productos")
    return listaProcesarDatos

def crearInforme(productos):
    pass
    #cargarINV

def crearArchivoTXT(lista, nombre_archivo):
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for elemento in lista:
                archivo.write(str(elemento) + "\n")
    except Exception as e:
        print("Error:", e)


rutaINFORME = ("informe.txt")
generarINFORME = crearInforme(open(rutaINFORME, "w", encoding="utf-8"))

def cargarArchivoINV():
    try:
        cargarINV
        #print(cargarINV)
        print(Fore.GREEN + "     -------------------------------------------")
        print(Fore.GREEN + "    |     Se cargó el archivo .inv con éxito!   |")
        print(Fore.GREEN + "     -------------------------------------------\n")

    except:
        print(Fore.RED + "     -------------------------------------")
        print(Fore.RED + "    |     ERROR: Datos no cargados        |")
        print(Fore.RED + "     -------------------------------------\n")

def cargarArchivoMOV():
    try:
        cargarMOVtalqueAgrega
        #print(cargarMOVtalqueAgrega[0])
        #print("___________________________________________\n")
        cargarMOVtalqueVende
        #print(cargarMOVtalqueVende)

        print(Fore.GREEN + "     ------------------------------------------")
        print(Fore.GREEN + "   |    Se cargó el archivo .mov con éxito!    |")
        print(Fore.GREEN + "     ------------------------------------------\n")

    except:
        print(Fore.RED + "    ------------------------------------------------------------------------")
        print(Fore.RED + "   |    ERROR: No se ha podido cargar el archivo .mov verifique la ruta     |")
        print(Fore.RED + "    ------------------------------------------------------------------------\n")

def crearInformeInventario():
    try:

        print(Fore.GREEN + "\n     Se ha creado el archivo de inventario inicial")
        crearArchivoTXT(cargarINV, "informe.txt")
        crearArchivoTXT(crearArchivoTXT, "informeActualizado.txt")
        #generarINFORME
        #print(generarINFORME)
        print(Fore.GREEN + "     --------------------------------------")
        print(Fore.GREEN + "   | Se creó el archivo Informe con éxito! |")
        print(Fore.GREEN + "     --------------------------------------\n")

    except:
        print(Fore.RED + "    ----------------------------------------------")
        print(Fore.RED + "   |    ERROR: No se ha podido crear el informe   |")
        print(Fore.RED + "    ----------------------------------------------\n")