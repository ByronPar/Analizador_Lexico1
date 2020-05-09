import os
import re

from byron_Manejadores.byron_beans.almacen import Almacen
from byron_Manejadores.byron_beans.calculadora import Calculadora

class Educacion:
    def __init__(self):

        self.elecciones = {  # mi diccionario menu
            "1": self.archivoEducacion,
            "2": self.archivoAlmacen,
            "3": self.regresar
        }

    def mostrar_menu(self):

        print("""
    ########################      Menu Educación      ########################

    1 Cargar Archivo .edu
    2 Cargar Archivo .almacen
    3 Regresar al Menu Principal
    """)

    def run(self, msj):  # Para Correr mi menu

        while True:
            self.mostrar_menu()
            eleccion = input("Seleccione una opción: ")
            accion = self.elecciones.get(eleccion)
            if accion:
                accion()
                break

            else:
                print("{0} no es una elección válida".format(eleccion))

    def regresar(self):  # Regreso a mi menu principal
        from Main import Menu
        Main = Menu()
        os.system("cls")
        Main.run()

    def archivoEducacion(self): #Cargo mi archivo .edu y genero mis datos con programación funcional
        ruta = input("\n Ingrese la dirección donde se encuentre su Archivo .edu     ")

        extension = "edu"
        # print(ruta[len(ruta)-7:len(ruta)])
        if ruta[len(ruta) - 3:len(ruta)] == extension:  # VERIFICO QUE SEA UNA Ruta con la extension adecuda

            if os.path.isfile(ruta):  # Verificar que el archivo exista

                contenido = ""  # print("\nEl archivo existe");
                f = open(ruta, 'r')
                contenido = f.read()  # leo el contenido de mi archivo
                self.splitDatos(contenido)  # print(contenido)
                f.close()



            # AQUI RETORNARE MI LINK CON MI ARCHIVO CREADO

            else:
                print("\nEl  archivo no existe ingrese una dirección valida");
                self.archivoEducacion()


        else:
            print("\n Debe Ingresar Un archivo con la extension solicitada,    VUELVA A INTENTARLO")
            self.archivoEducacion()

    def splitDatos(self,datos):
        pattern = re.compile("\n|:")
        instruccion = pattern.split(datos)

        # todas las instrucciones que mandare a mi nuevo file.edu_result
       #instruccionesNuevas=Calculadora.operar("",instruccion)
        #newrut = "C:\\Users\\HP ENVY\\Desktop\\calculadora.mascotas_result"
        #print(instruccionesNuevas)
        #arch = open(newrut, 'w')
        #arch.write(instruccionesNuevas)
        #arch.close()
        os.system("cls")
        msj = "asd"
        self.run(msj)










    def archivoAlmacen(self):
        ruta = input("\n Ingrese la dirección donde se encuentre su Archivo .almacen     ")

        extension = "almacen"
        # print(ruta[len(ruta)-7:len(ruta)])
        if ruta[len(ruta) - 7:len(ruta)] == extension:  # VERIFICO QUE SEA UNA Ruta con la extension adecuada

            if os.path.isfile(ruta):  # Verificar que el archivo exista

                contenido = ""  # print("\nEl archivo existe");
                f = open(ruta, 'r')
                contenido = f.read()  # leo el contenido de mi archivo
                self.splitDatosA(contenido)  # print(contenido)
                f.close()



            # AQUI RETORNARE MI LINK CON MI ARCHIVO CREADO

            else:
                print("\nEl  archivo no existe ingrese una dirección valida");
                self.archivoAlmacen()


        else:
            print("\n Debe Ingresar Un archivo con la extension solicitada,    VUELVA A INTENTARLO")
            self.archivoAlmacen()

    def splitDatosA(self,datos):
        pattern = re.compile("\n|:")
        instruccion = pattern.split(datos)

        # todas las instrucciones que mandare a mi nuevo file.almacen_result
        instruccionesNuevas=Almacen.operar("",instruccion)
        newrut = "C:\\Users\\HP ENVY\\Desktop\\almacenes.almacen_result"
        arch = open(newrut, 'w')
        arch.write(instruccionesNuevas)
        arch.close()
        os.system("cls")
        msj = "asd"
        self.run(msj)
