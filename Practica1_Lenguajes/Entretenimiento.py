import os
import re
import time

from byron_Manejadores.byron_beans.mascota import Mascota
from byron_Manejadores.byron_beans.mascota import Pajaro
from byron_Manejadores.byron_beans.mascota import Gato


class Entretenimiento:

    def __init__(self):

        self.elecciones = {  # mi diccionario menu
            "1": self.archivo,
            "2": self.regresar
        }

    def mostrar_menu(self):

        print("""
    ########################      Menu Entretenimiento      ########################

    1 Cargar Archivo .mascotas
    2 Regresar al Menu Principal
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

    def archivo(self):  # cargo mis  archivos y genero mis datos

        ruta = input("\n Ingrese la dirección donde se encuentre su Archivo .mascota     ")

        extension = "mascotas"
        # print(ruta[len(ruta)-8:len(ruta)])
        if ruta[len(ruta) - 8:len(ruta)] == extension:  # VERIFICO QUE SEA UNA Ruta con la extension adecuda

            if os.path.isfile(ruta):  # Verificar que el archivo exista

                contenido = ""  # print("\nEl archivo existe");
                f = open(ruta, 'r')
                contenido = f.read()  # leo el contenido de mi archivo
                self.splitDatos(contenido)  # print(contenido)
                f.close()



            # AQUI RETORNARE MI LINK CON MI ARCHIVO CREADO

            else:
                print("\nEl  archivo no existe ingrese una dirección valida");
                self.archivo()


        else:
            print("\n Debe Ingresar Un archivo con la extension solicitada,    VUELVA A INTENTARLO")
            self.archivo()

    def splitDatos(self, datos):  # METODO PARA SEPARAR MIS INSTRUCCIONES

        pattern = re.compile("\n|:")
        instruccion = pattern.split(datos)
        instruccionesNuevas = ""  # todas las instrucciones que mandare a mi nuevo file.mascotas_result
        indice = 0
        while indice < len(instruccion):
            if instruccion[indice] == "Crear_Pajaro":
                fechaActual = time.strftime("%d/%m/%y")
                horaActual = time.strftime("%H:%M:%S")
                pajaroNuevo = Pajaro(instruccion[indice + 1])
                instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "]  " + "Se Creo el pájaro " + \
                                      instruccion[indice + 1]
                Mascota.listarMascota(" ", pajaroNuevo)


            elif instruccion[indice] == "Puede_Entregar_Mensaje":
                fechaActual = time.strftime("%d/%m/%y")
                horaActual = time.strftime("%H:%M:%S")

                opcPuede = instruccion[indice + 1].split(sep=',')
                if Pajaro.puedeEntregarMensaje(" ", opcPuede[0], opcPuede[1], opcPuede[2]) == "si":
                    instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "]  " + \
                                          opcPuede[0] + " , Si puedo ir a dejar el mensaje"
                elif Pajaro.puedeEntregarMensaje(" ", opcPuede[0], opcPuede[1], opcPuede[2]) == "comida":
                    energia = Pajaro.energiaNecesitada(" ", opcPuede[0], opcPuede[1], opcPuede[2])
                    instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "]  " + \
                                          opcPuede[0] + " , Estoy exhausto. Dame de comer " + str(energia) + " para ir."
                elif Pajaro.puedeEntregarMensaje(" ", opcPuede[0], opcPuede[1], opcPuede[2]) == "muerto":
                    instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "]  " + \
                                          opcPuede[0] + " , Ya me mori"


            elif instruccion[indice] == "Enviar_Mensaje":
                fechaActual = time.strftime("%d/%m/%y")
                horaActual = time.strftime("%H:%M:%S")
                opcPuede = instruccion[indice + 1].split(sep=',')
                if Pajaro.enviarMensaje(" ", opcPuede[0], opcPuede[1], opcPuede[2]) == "si":

                    instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "]  " + \
                                          opcPuede[0] + " , Ya fui a dejar el msj a (" + opcPuede[1] + "," + opcPuede[
                                              2] + ")"
                elif Pajaro.enviarMensaje(" ", opcPuede[0], opcPuede[1], opcPuede[2]) == "comida":
                    energia = Pajaro.energiaNecesitada(" ", opcPuede[0], opcPuede[1], opcPuede[2])
                    instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "]  " + \
                                          opcPuede[0] + " , Estoy exhausto. Dame de comer " + str(energia) + " para ir."
                elif Pajaro.enviarMensaje(" ", opcPuede[0], opcPuede[1], opcPuede[2]) == "muerto":
                    instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "]  " + \
                                          opcPuede[0] + " , Ya me mori"
            elif instruccion[indice] == "Crear_Gato":
                fechaActual = time.strftime("%d/%m/%y")
                horaActual = time.strftime("%H:%M:%S")
                gatoNuevo = Gato(instruccion[indice + 1])
                instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "]  " + "Se Creo el gato " + \
                                      instruccion[indice + 1]
                Mascota.listarMascota(" ", gatoNuevo)

            elif instruccion[indice] == "Conviene_Comer_Raton":
                fechaActual = time.strftime("%d/%m/%y")
                horaActual = time.strftime("%H:%M:%S")

                opcPuede = instruccion[indice + 1].split(sep=',')
                if Gato.convieneComer(" ", opcPuede[0], opcPuede[1], opcPuede[2], opcPuede[3]) == "si":
                    instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "]  " + \
                                          opcPuede[0] + " , Si me conviene comerme al raton"
                elif Gato.convieneComer(" ", opcPuede[0], opcPuede[1], opcPuede[2], opcPuede[3]) == "comida":
                    instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "]  " + \
                                          opcPuede[0] + " , Esta muy lejos. No me conviene"
                elif Gato.convieneComer(" ", opcPuede[0], opcPuede[1], opcPuede[2], opcPuede[3]) == "muerto":
                    instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "]  " + \
                                          opcPuede[0] + " , Ya me mori"

            elif instruccion[indice] == "Enviar_Comer_Raton":
                fechaActual = time.strftime("%d/%m/%y")
                horaActual = time.strftime("%H:%M:%S")
                opcPuede = instruccion[indice + 1].split(sep=',')
                if Gato.convieneComer(" ", opcPuede[0], opcPuede[1], opcPuede[2], opcPuede[3]) == "si":
                    energianew = Gato.energiaNueva(" ", opcPuede[0], opcPuede[1], opcPuede[2], opcPuede[3])
                    instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "]  " + \
                                          opcPuede[0] + " , Ya me comí al ratón, ahora mi energía es " + str(energianew)
                elif Gato.convieneComer(" ", opcPuede[0], opcPuede[1], opcPuede[2], opcPuede[3]) == "comida":
                    energia = Gato.energiaNecesitada(" ", opcPuede[0], opcPuede[1], opcPuede[2], opcPuede[3])
                    instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "]  " + \
                                          opcPuede[0] + " , Estoy exhausto. Dame de comer " + str(energia) + " para ir."
                elif Gato.convieneComer(" ", opcPuede[0], opcPuede[1], opcPuede[2], opcPuede[3]) == "muerto":
                    instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "]  " + \
                                          opcPuede[0] + " , Ya me mori"

            elif instruccion[indice] == "Dar_de_Comer":
                fechaActual = time.strftime("%d/%m/%y")
                horaActual = time.strftime("%H:%M:%S")
                opcPuede = instruccion[indice + 1].split(sep=',')

                if Mascota.compComida(" ", opcPuede[0]) == "no existe":
                    print("\n Mascota no Existe")
                elif Mascota.compComida(" ", opcPuede[0]) == "muerto":
                    instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "]  " + \
                                          opcPuede[0] + " , Muy tarde. Ya me morí."
                elif Mascota.compComida(" ", opcPuede[0]) == "si":
                    energianew = Mascota.darComida(" ", opcPuede[0], opcPuede[1])
                    instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "]  " + \
                                          opcPuede[0] + " , Gracias. Ahora mi energia es " + str(energianew)

            elif instruccion[indice] == "Resumen_Mascota":
                fechaActual = time.strftime("%d/%m/%y")
                horaActual = time.strftime("%H:%M:%S")
                cadenanew = Mascota.resumenMascota(" ", instruccion[indice + 1])
                instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "]  " + cadenanew

            elif instruccion[indice] == "Resumen_Global":
                fechaActual = time.strftime("%d/%m/%y")
                horaActual = time.strftime("%H:%M:%S")
                cadenanew = Mascota.resumenGlobal(" ")
                instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "]  --------------------------------------- RESUMEN GLOBAL --------------------------------------- " + cadenanew + "\n[" + fechaActual + "  " + horaActual + "]  ---------------------------------------------------------------------------------------------- "
                indice = indice - 1

            if (indice + 2) <= len(instruccion):
                indice = indice + 2
        newrut="C:\\Users\\HP ENVY\\Desktop\\ResumenMascotas.mascotas_result"
        arch = open(newrut, 'w')
        arch.write(instruccionesNuevas)
        arch.close()
        os.system("cls")
        msj="asd"
        self.run(msj)

    def regresar(self):  # Regreso a mi menu principal
        from Main import Menu
        Main = Menu()
        os.system("cls")
        Main.run()
