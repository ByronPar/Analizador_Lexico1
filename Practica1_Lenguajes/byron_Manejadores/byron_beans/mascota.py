from cmath import sqrt
import time

listaMascotas = []  # VARIABLE GLOBAL PARA ALMACENAR MIS MSACOTAS


class Mascota:
    nombre = ""
    energia = 1
    estado = ""
    posX = 0.0
    posY = 0.0
    tipo = ""

    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 1
        self.estado = "vivo"
        self.posX = 0.0
        self.posY = 0.0

    def listarMascota(self, masc):
        global listaMascotas
        listaMascotas.append(masc)

    def compComida(self, nombre):
        global listaMascotas
        for i in listaMascotas:
            mascota = i
            if mascota.nombre == nombre:
                if mascota.estado == "vivo":
                    return "si"



                else:
                    return "muerto"
        return "no existe"

    def darComida(self, nombre, peso):
        global listaMascotas
        indice = 0
        for i in listaMascotas:
            mascota = i
            if mascota.nombre == nombre:
                if mascota.tipo == "Gato":
                    mascota.energia = int(mascota.energia) + 12 + int(peso)
                    listaMascotas[indice] = mascota
                    return mascota.energia

                elif mascota.tipo == "Pajaro":
                    mascota.energia = mascota.energia + (int(peso) * 4)
                    listaMascotas[indice] = mascota
                    return mascota.energia
            indice = indice + 1

    def resumenMascota(self, nombre):
        global listaMascotas
        cadena = ""
        for i in listaMascotas:
            mascota = i
            if mascota.nombre == nombre:
                cadena = cadena + nombre + " , " + "Energia: " + str(mascota.energia) + " , X: " + str(
                    mascota.posX) + " , Y: " + str(
                    mascota.posY) + " , Tipo: " + mascota.tipo + " , Estado: " + mascota.estado
                return cadena

    def resumenGlobal(self):
        fechaActual = time.strftime("%d/%m/%y")
        horaActual = time.strftime("%H:%M:%S")
        global listaMascotas
        cadena = ""
        for i in listaMascotas:
            mascota = i
            cadena = cadena + "\n[" + fechaActual + "  " + horaActual + "]  " + mascota.nombre + " , " + "Energia: " + str(
                mascota.energia) + " , X: " + str(mascota.posX) + " , Y: " + str(
                mascota.posY) + " , Tipo: " + mascota.tipo + " , Estado: " + mascota.estado
        return cadena

    def CalcDistancia(self, p1X, p2X, p1Y, p2Y):
        complejo = sqrt((p1X - p2X) ** 2 + (p1Y - p2Y) ** 2)
        real = complejo.real
        real2 = round(real)
        return int(real2)


class Pajaro(Mascota):
    tipo = "Pajaro"

    def __init__(self, nombre):
        Mascota.__init__(self, nombre)
        self.tipo = "Pajaro"

    def puedeEntregarMensaje(self, nombre, posx, posy):
        global listaMascotas
        for i in listaMascotas:

            mascota = i
            if mascota.nombre == nombre:
                if mascota.tipo == "Pajaro":
                    distanciaAdeja = mascota.CalcDistancia(int(mascota.posX), int(posx), int(mascota.posY),
                                                           int(posy))  # distancia en kilometros
                    energiaAdejar = 10 + distanciaAdeja
                    if mascota.energia == 0:
                        return "muerto"
                    elif mascota.energia >= energiaAdejar:
                        return "si"
                    elif mascota.energia < energiaAdejar:
                        return "comida"

    def enviarMensaje(self, nombre, posx, posy):
        global listaMascotas
        indice = 0
        est = "muerto"
        for i in listaMascotas:
            mascota = i
            if mascota.nombre == nombre:
                if mascota.tipo == "Pajaro":
                    distanciaAdeja = mascota.CalcDistancia(int(mascota.posX), int(posx), int(mascota.posY), int(posy))
                    energiaAdejar = 10 + int(distanciaAdeja)
                    if mascota.energia == 0:
                        return "muerto"
                    elif mascota.energia >= energiaAdejar:
                        mascota.energia = mascota.energia - energiaAdejar
                        mascota.posX = posx
                        mascota.posY = posy
                        if mascota.energia == 0:
                            mascota.estado = est
                            listaMascotas[indice] = mascota
                            return "si"
                        else:
                            listaMascotas[indice] = mascota
                            return "si"
                    elif mascota.energia < energiaAdejar:
                        return "comida"
            indice = indice + 1

    def energiaNecesitada(self, nombre, posx, posy):
        global listaMascotas
        for i in listaMascotas:
            mascota = i
            if mascota.nombre == nombre:
                if mascota.tipo == "Pajaro":
                    distanciaAdeja = mascota.CalcDistancia(int(mascota.posX), int(posx), int(mascota.posY), int(posy))
                    energiaAdejar = 10 + int(distanciaAdeja)
                    necesito = energiaAdejar - mascota.energia
                    return necesito


class Gato(Mascota):
    tipo = "Gato"

    def __init__(self, nombre):
        Mascota.__init__(self, nombre)
        self.tipo = "Gato"

    def convieneComer(self, nombre, posx, posy, peso):
        global listaMascotas
        for i in listaMascotas:
            mascota = i
            if mascota.nombre == nombre:
                if mascota.tipo == "Gato":
                    if int(peso) == 0:
                        distanciaAdeja = mascota.CalcDistancia(int(mascota.posX), int(posx), int(mascota.posY),
                                                               int(posy))
                        energiaAdejar = (distanciaAdeja / 2)
                        if mascota.energia == 0:
                            return "muerto"
                        elif mascota.energia >= energiaAdejar:
                            return "si"
                        elif mascota.energia < energiaAdejar:
                            return "comida"

                    distanciaAdeja = mascota.CalcDistancia(int(mascota.posX), int(posx), int(mascota.posY), int(posy))
                    energiaAdejar = int(distanciaAdeja / 2) - 12 - int(peso)
                    if mascota.energia == 0:
                        return "muerto"
                    elif mascota.energia >= int(energiaAdejar):
                        return "si"
                    elif mascota.energia < int(energiaAdejar):
                        return "comida"

    def energiaNueva(self, nombre, posx, posy, peso):
        global listaMascotas
        indice = 0
        est = "muerto"
        for i in listaMascotas:
            mascota = i
            if mascota.nombre == nombre:
                if mascota.tipo == "Gato":
                    distanciaAdeja = mascota.CalcDistancia(int(mascota.posX), int(posx), int(mascota.posY), int(posy))
                    energiaAdejar = int(distanciaAdeja / 2) - 12 - int(peso)
                    mascota.energia = mascota.energia - (energiaAdejar)
                    mascota.posX = posx
                    mascota.posY = posy
                    print(mascota.energia)
                    if mascota.energia == 0:
                        print(mascota.energia)
                        mascota.estado = est
                        print(mascota.energia)
                        listaMascotas[indice] = mascota
                        print(mascota.energia)
                        return mascota.energia
                    else:
                        listaMascotas[indice] = mascota
                        return mascota.energia

            indice = indice + 1

    def energiaNecesitada(self, nombre, posx, posy, peso):
        global listaMascotas
        for i in listaMascotas:
            mascota = i
            if mascota.nombre == nombre:
                if mascota.tipo == "Gato":
                    distanciaAdeja = mascota.CalcDistancia(int(mascota.posX), int(posx), int(mascota.posY), int(posy))
                    energiaAdejar = int(distanciaAdeja / 2) - 12 - int(peso)
                    necesito = energiaAdejar - mascota.energia + 0
                    if necesito >= 1:
                        return necesito
                    necesito = 1
                    return necesito
