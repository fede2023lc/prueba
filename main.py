"""
SkyRoute - Sistema de Gestión de Pasajes Aéreos


Propósito:
Este sistema de consola permite gestionar clientes, destinos y ventas de pasajes
para la empresa ficticia SkyRoute S.R.L. Además, incluye una opción de “botón de
arrepentimiento” para anular ventas recientes, conforme a la Ley 24.240.

Integrantes:
Dante Coledas  		      DNI: 43601086
Federico López 		      DNI: 35994586
Maximiliano Schaufele 	DNI: 33101618
Emanuel Toledo 		      DNI: 31600022
Mariela Yacci   	  	  DNI 22443856

Instrucciones:
1. Ejecutar el programa con Python 3.
2. Navegar el menú mediante números según las opciones presentadas.
3. Seguir los mensajes en consola para cada acción.


"""

#Primero unas variables auxiliares que usaramos mas adelante para realizar un contador
#es necesario que quedé fuera del while para que vuelva a valores 0 empieza el ciclo nuevamente
contadorClientes= 0
contadorVentas= 0
contadorDestinos= 0
contadorVentasAnuladas= 0
#Segundo definimos una estructura iterativa con un while True: para que repita continuamente el menú inicial
while True: #Finaliza el ciclo con un break en la opción 8.SALIR
#Mensaje de Bienvenida y mostrar opciones mediante  Estructura secuencial print()
    print("==============================")
    print("Bienvenido a skyroute")
    print("1. Gestionar Clientes")
    print("2. Gestionar Ventas")
    print("3. Gestionar Destinos")
    print("4. Consultar Ventas")
    print("5. Boton de Arrepentimiento")
    print("6. Reportes por sesión")
    print("7. Acerca del Sistema")
    print("8. SALIR")
    print("==============================")
#se crea una variable "opcion" y se solicita mediante input y un mensaje strg "ingresar alguna opcion"
    opcion= input("ingrese opción:")
    print(f"Seleccionó opción: {opcion}")
#se abre un clico condicional de if, elif y else para acceder los submenús
    if opcion == "1":
            while True:
                print("Gestionar clientes")
                print("1. Agregar nuevo cliente")
                print("2. Modificar cliente")
                print("3. Eliminar cliente")
                print("4. Ver clientes")
                print("5. Atrás")
                opcion= input("Ingrese opción:")
                print(f"Seleccionó opción: {opcion}")
#se abre otro ciclo if, elif y else para elegir opciones del submenú
                if opcion=="1":
                    print("Agregar nuevo cliente")
                    print("Ingrese los datos del cliente")
                    razonSocial= input("Razón Social:") #creación de variables instanciadas por un input
                    cuit= input("CUIT:")
                    mail= input("Mail:")
                    contadorClientes += 1 #un contador para la cantidad de clientes nuevo, se usa para opcion 6.Reportes
#Impresión de mensaje string con variables, que comunicá al usuario la creación de un nuevo clientes y sus datos
                    print(f"Usted ingresó nuevo cliente: Razón Social:{razonSocial} CUIT:{cuit} mail: {mail}")
                    print("==============================")
#siguiente subopción, utilizamos elif correspondiente al if con la misma tabulación para acceder a opción 2
                elif opcion=="2":
                    print("Modificar cliente")
                    cuit1= input("ingrese cuit:") # creamos variables instanciadas por el usurio con un input para usarlas en un mensaje print()
                    razonSocial= input("Razón Social:")
                    cuit= input("CUIT:")
                    mail= input("Mail:")
                    print(f"Usted modificó cliente: Razón Social:{razonSocial} CUIT:{cuit} mail: {mail}")
                    print("==============================")
                elif opcion=="3":
                    print("Eliminar cliente")
                    cuit= input("ingrese cuit:")
                    print(f"Usted eliminó cliente cuit: {cuit}")
                    print("==============================")
                    contadorClientes -= 1
                elif opcion=="4":
                    print("Ver clientes")
                    print("Lista de clientes")
                    for i in range(5):
                        print(f"Cliente {i+1}")
                    print("==============================")
                elif opcion=="5":
                    print("Seleccionó 5.Atrás")
                    break #utilizamos break para salir del sub-menú
                else: #para cualquier otra opción fuera del rango del sub-menú
                    print("Opción no valida")
                    print("==============================")
    elif opcion=="2":#elif del condicional if de la misma tabulación. El if principal de la pantalla de inicio.
        while True:
            print("Gestionar Ventas")
            print("1. Agregar nueva venta")
            print("2. Eliminar venta")
            print("3. Ver ventas por mes y año")
            print("4. Atrás")
            opcion= input("ingrese opción:")#se muestran opciones mediante print y piden opcion mediante input
            if opcion=="1": #nuevo if para el sub-menú
                print("Seleccionó: Agregar nueva venta")
                print("Ingrese los datos de la venta")
                codigoVenta= input("Código de venta:")
                fechadeViaje= input("Fecha de viaje:")
                cuit= input("CUIT del cliente:")
                destino= input("Destino:")
                print(f"Usted ingresó nueva venta: \n Código de venta:{codigoVenta} \n Fecha de viaje:{fechadeViaje} \n Cliente CUIT:{cuit} \n Destino:{destino}")
                contadorVentas += 1 #contador de ventas (se usa en 6. Reporte)
                print("==============================")
            elif opcion=="2":
                print("seleccionó: Eliminar venta")
                codigoVenta= input("ingrese código de venta:")
                print(f"usted eliminó venta código:{codigoVenta}")
                contadorVentas -= 1 #contador de ventas en caso que se eliminé alguna
                print("==============================")
            elif opcion=="3":
                print("seleccionó: Ver ventas por mes y año")
                mes= input("ingrese mes:")
                anio= input("ingrese año:")
                print(f"Lista de ventas del mes:{mes} y año:{anio}")
                for i in range(5):
                    print(f"Venta {i+1}")
                print("==============================")
            elif opcion=="4":
                print("Seleccionó: Atrás")
                break
            else:
                print("Opción no valida")
                print("==============================")
  #siguiente elif para el menú de inicio
    elif opcion=="3":
        while True:
            print("Gestionar Destinos")
            print("1. Agregar nuevo destino")
            print("2. Modificar destino")
            print("3. Eliminar destino")
            print("4. Ver destinos")
            print("5. Atrás")
            opcion= input("Ingrese opción:")
            if opcion=="1":#nuevo if para elegir opcion en el sub-menú
                print("seleccionó: Agregar nuevo destino")
                print("Ingrese los datos del destino")
                codigoDestino= input("Código de destino:")
                ciudad= input("Ciudad:")
                pais= input("País:")
                costoBase= input("Costo base:")
                print(f"Usted ingresó nuevo destino: \n Código de destino:{codigoDestino} Ciudad:{ciudad} País:{pais} Costo base:{costoBase}")
                contadorDestinos += 1 #contador de destinos (se usa para 6.Reportes)
                print("==============================")
            elif opcion=="2":
                print("Seleccionó: Modificar destino")
                codigoDestino= input("Ingrese código de destino:")
                print("Ingrese los nuevos datos del destino")
                ciudad= input("Ciudad:")
                pais= input("País:")
                costoBase= input("Costo base:")
                print(f"Usted modificó destino código:{codigoDestino} \n Ciudad:{ciudad} País:{pais} Costo base:{costoBase}")
                print("==============================")
            elif opcion=="3":
                print("Seleccionó: Eliminar destino")
                codigoDestino= input("Ingrese código de destino:")
                print(f"Usted eliminó destino código:{codigoDestino}")
                contadorDestinos -= 1
                print("==============================")
            elif opcion=="4":
                print("Seleccionó: Ver destinos")
                print("Lista de destinos")
                for i in range(5):
                    print(f"Destino {i+1}")
                print("==============================")
            elif opcion=="5":
                print("Seleccionó: Atrás")
                break
            else:
                print("Opción no valida")
                print("==============================")
    elif opcion=="4": #elif para mostrar sub-menú "consulta de Ventas"
        while True:
            print("Consultar Ventas")
            print("1. Consultar ventas por cliente") #se puede consultar por cliente, destino o rango de fechas
            print("2. Consultar ventas por destino")
            print("3. Consultar ventas por rango de fechas")
            print("4. Atrás")
            opcion= input("Ingrese opción:") #secuencial input para la selección de opcion del submenú
            if opcion=="1": #condicional if para mostrar la opcion elegida
                print("Seleccionó: Consultar ventas por cliente")
                cuit= input("Ingrese cuit:") #ingreso del cuit del cliente de cual se quiere consultar
                print(f"Lista de ventas del cliente cuit:{cuit}")
                print("==============================")
            elif opcion=="2":
                print("Seleccionó: Consultar ventas por destino")
                codigoDestino= input("Ingrese código de destino:")
                print(f"Lista de ventas del destino código:{codigoDestino}")
                print("==============================")
            elif opcion=="3":
                print("Seleccionó: Consultar ventas por rango de fechas")
                fechaDesde= input("Ingrese fecha desde (dd/mm/aaaa):")#ingreso de fechas informando formarto pedido
                fechaHasta= input("Ingrese fecha hasta (dd/mm/aaaa):")
                print(f"Lista de ventas desde la fecha:{fechaDesde} hasta la fecha:{fechaHasta}")
                print("==============================")
            elif opcion=="4":
                print("Seleccionó: Atrás")
                break
            else:
                print("Opción no valida")
                print("==============================")
    elif opcion=="5":#elif del if del menú inicial
        while True:
            print("Boton de Arrepentimiento")
            print("1. Anular venta por Botón de Arrepentimiento")
            print("2. Ver ventas anuladas por Botón de arrepentimiento")
            print("3. Atrás")
            opcion= input("ingrese opción:")
            if opcion=="1":
                print("Anular venta por Botón de Arrepentimiento")
                codigoventa= input("Ingrese código de venta:")
                try:
                    diashabilesdesdelacompra= int(input("Ingrese días hábiles desde la compra:")) #convierto a int para hacer una comparación aricmetica en if siguente
                    if 0<diashabilesdesdelacompra<=60: #defino el rango de días validos desde 1 a 60 inclusive
                        print(f"Usted anuló la venta código:{codigoventa}")
                        contadorVentasAnuladas += 1
                    elif diashabilesdesdelacompra>60:
                        print(f"Usted no puede anular la venta código:{codigoventa}")
                    else:
                        print("Error") #para días no validos tipo numericos imprime error y sigue con el submenú.
                except:
                    print("Error: Ingresas días con carácteres numéricos sin letras ni simbolos")
                print("==============================")
            elif opcion=="2":
                print("Seleccionó: Ver ventas anuladas por Botón de arrepentimiento")
                print(f"Total de ventas anuladas: {contadorVentasAnuladas}") #se muestran las cantidad de ventas anuladas
                print("Lista de ventas anuladas")
                for i in range(contadorVentasAnuladas):
                    print(f"venta anulada {i+1}")
                print("==============================")
            elif opcion=="3":
                print("Seleccionó: Atrás")
                break
            else:
                print("Opción no valida")
                print("==============================")
    elif opcion=="6":
        print("Reportes por sesión") #aprovechamos los incrementables variable += 1, para hacer un contador de nuevos clientes, ventas y destinos
        print(f"1. Clientes nuevos: {contadorClientes}")#cada vez que se haya creado un cliente la variable contadorCliente iba aunmentado +1 por vez.
        print(f"2. Ventas nuevas: {contadorVentas}")#Estas variables se definen al princio igualadas a 0 y fuera del while true: para que no se vuelvan a hacer cero
        print(f"3. Destinos nuevos: {contadorDestinos}")
        print(f"4. Ventas anuladas por botón de Arrepentimiento: {contadorVentasAnuladas}")
    elif opcion=="7":
        print("Acerca del Sistema") #breve mensaje para los usuarios
        print("Sistema de gestión de ventas de SkyRoute desarrollado por GrupoPy S.R.L. ")
    elif opcion == "8": #Este elif, es la única salida del while True: y la única manera de salir del sistema de gestión.
        print("Seleccionó SALIR. \nGracias por usar Sistema de Gestión de Ventas de Skyroute. Hasta luego.")
        break   #este comando break termina la iteración while True: saliendo del programa
    else:
        print("Opción no valida.")#Aquí las opciones no validas devuelven al usuario al mismo menú inicio por el cliclo while True:
