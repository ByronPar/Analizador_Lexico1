import msvcrt
import os
import sys
from datetime import time

from Educacion import Educacion
from Entretenimiento import Entretenimiento


class Menu:
    def __init__(self):
        self.Educacion = Educacion()
        self.Entretenimiento = Entretenimiento()
        self.elecciones = {  # mi diccionario menu
            "1": self.entretenimiento,
            "2": self.educacion,
            "3": self.quit
        }

    def mostrar_menu(self):

        print("""
########################      Menu Principal      ########################

1 Menu Entretenimiento
2 Menu Educación
3 Salir
""")

    def run(self):  # Para Correr mi menu

        while True:
            self.mostrar_menu()
            eleccion = input("Seleccione una opción: ")
            accion = self.elecciones.get(eleccion)
            if accion:
                accion()
                break

            else:
                print("{0} no es una elección válida".format(eleccion))

    def entretenimiento(self):
        msj = "hola"
        os.system("cls")
        self.Entretenimiento.run(msj)

    def educacion(self):
        msj = "hola"
        self.Educacion.run(msj)

    def quit(self):
        print("\n FIN DE LA APLICACIÓN  ")
        sys.exit(0)


class Datos:
    def run(self):  # Para Correr mi menu de Información
        self.mostrar_menu()
        input("\n Presione Enter Para Continuar")
        os.system("cls")
        if __name__ == "__main__":
            Menu().run()

    def mostrar_menu(self):
        print("""
    ########################      DATOS DEL ESTUDIANTE      ########################


           Lenguajes formales y de Programación
           
           Sección :  A+
                                                                     Practica No.1
           Byron Josué Par Rancho  
           
           Carnet : 201701078
           
           
    ########################                                 ########################
        
        
           
    """)


# if __name__ == "__main__":
#   Menu().run()

if __name__ == "__main__":
    Datos().run()
