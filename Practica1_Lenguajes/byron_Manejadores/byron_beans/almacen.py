import time
listaVariables=[]
listaAlmacen=[]


class Variable:
    def __init__(self, id,posicion):
        self.id = id
        self.posicion = posicion




class Almacen:

    def operar(self, lista):
        global posicionAlmacen
        global listaVariables
        global listaAlmacen

        listaInstrucciones = lista




        listaVariables = []  # variable global para almacenar mis cadenas y posicion del puntero (donde se almaceno el ultimo caracter +1 )
        listaAlmacen = []  # variable global para almacenar mis caracteres y su posicion
        posicionAlmacen = 1
        instruccionesNuevas = ""  # todas las instrucciones que mandare a mi nuevo file.almacen_result


        x=1
        listaAlmacen.append(x)




        indice = 0
        while indice < len(listaInstrucciones):
            listaAlmacen[0]=posicionAlmacen


            if listaInstrucciones[indice] == "Declarar":

                par=listaInstrucciones[indice+1].split(sep=',')
                contar = 0
                for i in par[1]:
                    contar = contar + 1

                listaAlmacen.append(contar)

                variabl = Variable(par[0], posicionAlmacen)#posicionAlmacen=posicion Variable
                listaVariables.append(variabl)
                posicionAlmacen=posicionAlmacen+1
                for i in par[1]:
                    listaAlmacen.append(i)
                    posicionAlmacen=posicionAlmacen+1
                listaAlmacen[0] = posicionAlmacen




            elif listaInstrucciones[indice] == "Concatenar":
                ver1=False
                ver2=False
                pos1=0
                pos2=0

                palabras=listaInstrucciones[indice+1].split(sep=',')
                for i in listaVariables:
                    if i.id==palabras[0]:
                        pos1=i.posicion
                        ver1=True

                for i in listaVariables:
                    if i.id == palabras[1]:
                        pos2=i.posicion
                        ver2 = True


                if (ver1==True) and (ver2==True):
                    listaAlmacen.append(listaAlmacen[pos1] + listaAlmacen[pos2])
                    posicionAlmacen=posicionAlmacen+1
                    valor=listaAlmacen[pos1]
                    while valor>0:
                        listaAlmacen.append(listaAlmacen[pos1+1])
                        pos1=pos1+1
                        posicionAlmacen=posicionAlmacen+1
                        valor=valor-1

                    valor=listaAlmacen[pos2]
                    while valor>0:
                        listaAlmacen.append(listaAlmacen[pos2+1])
                        pos2=pos2+1
                        posicionAlmacen=posicionAlmacen+1
                        valor=valor-1
                        listaAlmacen[0] = posicionAlmacen


            elif listaInstrucciones[indice] == "Posicion_cadena":
                fechaActual = time.strftime("%d/%m/%y")
                horaActual = time.strftime("%H:%M:%S")

                for i in listaVariables:

                    if i.id==listaInstrucciones[indice+1]:
                        instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "]  " + \
                                              listaInstrucciones[indice + 1] + ", Pos:  "+str(i.posicion)


            elif listaInstrucciones[indice] == "Tamanio":
                fechaActual = time.strftime("%d/%m/%y")
                horaActual = time.strftime("%H:%M:%S")
                for i in listaVariables:
                    if i.id==listaInstrucciones[indice+1]:
                        pos=i.posicion
                        instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "]  " + \
                                              listaInstrucciones[indice + 1] + ", Tam:  "+str(listaAlmacen[pos])

            elif listaInstrucciones[indice] == "Imprimir":
                fechaActual = time.strftime("%d/%m/%y")
                horaActual = time.strftime("%H:%M:%S")

                for i in listaVariables:
                    if i.id==listaInstrucciones[indice+1]:
                        pos=i.posicion
                        valor=listaAlmacen[pos]
                        while valor>0:
                            instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "]  " + \
                                              listaInstrucciones[indice + 1] + ", "+str((pos+1))+","+listaAlmacen[pos+1]
                            pos=pos+1
                            valor=valor-1





            elif listaInstrucciones[indice] == "Generar_grafo":
                fechaActual = time.strftime("%d/%m/%y")
                horaActual = time.strftime("%H:%M:%S")
                indice=indice+1



            if (indice + 2) <= len(listaInstrucciones):
                indice = indice + 2


        return instruccionesNuevas
