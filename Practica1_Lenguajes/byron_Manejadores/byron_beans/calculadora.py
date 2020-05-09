import time

listaValores = []



class Valor:
    def __init__(self, nombre, postija, valor):
        self.nombre = nombre
        self.postfija = postija
        self.valor = valor


class Calculadora:

    def operar(self, lista):
        global listaValores
        global  posvector

        listaInstrucciones = lista

        indice = 0
        while indice < len(listaInstrucciones):

            if listaInstrucciones[indice] == "Variable":
                par = listaInstrucciones[indice + 1].split(sep=',')
                nombr = par[0]

                vectorExpre = []
                cadenita=''
                hacerya=0
                for i in par[1]:
                    sise = False
                    try:
                        poker=int(i)
                        cadenita=cadenita+i
                        sise = True
                        hacerya=1
                    except:
                        if hacerya == 1:
                            vectorExpre.append(cadenita)
                            cadenita = ''
                            hacerya=0



                    if sise==False:
                        if i==" " or i=="" or i=='' or i==' ':
                            lk=" "
                        else:
                            vectorExpre.append(i)
                poster = Calculadora.postfija("", vectorExpre)
                vectPos=Calculadora.vectPost("",vectorExpre)
                val = Calculadora.valor("", vectPos)
                alistar = Valor(nombr, poster, val)
                listaValores.append(alistar)


            elif listaInstrucciones[indice] == "Postfija":
                fechaActual = time.strftime("%d/%m/%y")
                horaActual = time.strftime("%H:%M:%S")
                expre = Calculadora.postfija("", listaInstrucciones[indice + 1])
                expre2 = ""
                for i in expre:
                    expre2 = expre2 + i + " "

                instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "]  Postfija:  " + expre2

            elif listaInstrucciones[indice] == "Incrementar":
                for i in listaValores:
                    valor = i
                    if valor.nombre == listaInstrucciones[indice + 1]:
                        valor.valor = valor.valor + 1



            elif listaInstrucciones[indice] == "Mitad":
                for i in listaValores:
                    valor = i
                    if valor.nombre == listaInstrucciones[indice + 1]:
                        valor.valor = valor.valor / 2



            elif listaInstrucciones[indice] == "Triple":
                for i in listaValores:
                    valor = i
                    if valor.nombre == listaInstrucciones[indice + 1]:
                        valor.valor = valor.valor * 3

            elif listaInstrucciones[indice] == "Positivo":
                for i in listaValores:
                    valor = i
                    if valor.nombre == listaInstrucciones[indice + 1]:
                        valor.valor = abs(valor.valor)

            elif listaInstrucciones[indice] == "Negativo":
                for i in listaValores:
                    valor = i
                    if valor.nombre == listaInstrucciones[indice + 1]:
                        valor.valor = -(abs(valor.valor))

            elif listaInstrucciones[indice] == "Potencia":
                pot = 0
                par = listaInstrucciones[indice + 1].split(sep=',')
                post1 = Calculadora.postfija("", par[0])
                post2 = Calculadora.postfija("", par[1])
                val1 = Calculadora.valor("", post1)
                val2 = Calculadora.valor("", post2)
                pot = val1 ** val2
                instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "]  Potencia:  " + str(
                    pot)

            elif listaInstrucciones[indice] == "Imprimir":
                for i in listaValores:
                    valor = i
                    if valor.nombre == listaInstrucciones[indice + 1]:
                        instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "] " + valor.nombre + " , " + str(
                            valor.valor)

            elif listaInstrucciones[indice] == "Imprimir_Mensaje":
                for i in listaValores:
                    valor = i
                    if valor.nombre == listaInstrucciones[indice + 1]:
                        instruccionesNuevas = instruccionesNuevas + "\n[" + fechaActual + "  " + horaActual + "] " + str(
                            listaInstrucciones[indice + 1])

            if (indice + 2) <= len(listaInstrucciones):
                indice = indice + 2

        return instruccionesNuevas


    def vectPost(self,expresion):
        vectPost=[]
        pila = []
        post = ""
        for i in expresion:
            if i == "*" or i == "/":
                hecho = False

                while hecho == False:
                    if pila:
                        pExp = 2
                        val = pila[-1]
                        if val == "*" or val == "/":

                            pPil2 = 2
                            if pExp > pPil2:
                                pila.append(i)
                                hecho = True
                            else:
                                vectPost.append(pila.pop())
                        elif val == "+" or val == "-":
                            pPil2 = 1
                            if pExp > pPil2:
                                pila.append(i)
                                hecho = True
                            else:
                                vectPost.append(pila.pop())
                        elif val == "(":
                            pPil2 = 0
                            if pExp > pPil2:
                                pila.append(i)
                                hecho = True
                            else:
                                vectPost.append(pila.pop())
                    else:
                        pila.append(i)
                        hecho = True

            elif i == "+" or i == "-":
                hecho = False

                while hecho == False:
                    if pila:
                        pExp = 1
                        val = pila[-1]
                        if val == "*" or val == "/":

                            pPil2 = 2
                            if pExp > pPil2:
                                pila.append(i)
                                hecho = True
                            else:
                                vectPost.append(pila.pop())
                        elif val == "+" or val == "-":
                            pPil2 = 1
                            if pExp > pPil2:
                                pila.append(i)
                                hecho = True
                            else:
                                vectPost.append(pila.pop())
                        elif val == "(":
                            pPil2 = 0
                            if pExp > pPil2:
                                pila.append(i)
                                hecho = True
                            else:
                                vectPost.append(pila.pop())
                    else:
                        pila.append(i)
                        hecho = True

            elif i == "(":
                hecho = False

                while hecho == False:
                    if pila:
                        pExp = 5
                        val = pila[-1]
                        if val == "*" or val == "/":

                            pPil2 = 2
                            if pExp > pPil2:
                                pila.append(i)
                                hecho = True
                            else:
                                vectPost.append(pila.pop())
                        elif val == "+" or val == "-":
                            pPil2 = 1
                            if pExp > pPil2:
                                pila.append(i)
                                hecho = True
                            else:
                                vectPost.append(pila.pop())
                        elif val == "(":
                            pPil2 = 0
                            if pExp > pPil2:
                                pila.append(i)
                                hecho = True
                            else:
                                vectPost.append(pila.pop())
                    else:
                        pila.append(i)
                        hecho = True

            elif i == ")":

                while pila[-1] != "(":
                    vectPost.append(pila.pop())
                pila.pop()
            elif i == " ":
                kl = ""
            else:  # cuando sea un número
                if pila:
                    vectPost.append(pila.pop())

        while pila:
            vectPost.append(pila.pop())

        return vectPost



    def postfija(self, expresion):


        pila = []
        post = ""
        for i in expresion:
            if i == "*" or i == "/":
                hecho = False

                while hecho == False:
                    if pila:
                        pExp = 2
                        val = pila[-1]
                        if val == "*" or val == "/":

                            pPil2 = 2
                            if pExp > pPil2:
                                pila.append(i)
                                hecho = True
                            else:
                                post = post + str(pila.pop())
                        elif val == "+" or val == "-":
                            pPil2 = 1
                            if pExp > pPil2:
                                pila.append(i)
                                hecho = True
                            else:
                                post = post + str(pila.pop())
                        elif val == "(":
                            pPil2 = 0
                            if pExp > pPil2:
                                pila.append(i)
                                hecho = True
                            else:
                                post = post + str(pila.pop())
                    else:
                        pila.append(i)
                        hecho = True

            elif i == "+" or i == "-":
                hecho = False

                while hecho == False:
                    if pila:
                        pExp = 1
                        val = pila[-1]
                        if val == "*" or val == "/":

                            pPil2 = 2
                            if pExp > pPil2:
                                pila.append(i)
                                hecho = True
                            else:
                                post = post + str(pila.pop())
                        elif val == "+" or val == "-":
                            pPil2 = 1
                            if pExp > pPil2:
                                pila.append(i)
                                hecho = True
                            else:
                                post = post + str(pila.pop())
                        elif val == "(":
                            pPil2 = 0
                            if pExp > pPil2:
                                pila.append(i)
                                hecho = True
                            else:
                                post = post + str(pila.pop())
                    else:
                        pila.append(i)
                        hecho = True

            elif i == "(":
                hecho = False

                while hecho == False:
                    if pila:
                        pExp = 5
                        val = pila[-1]
                        if val == "*" or val == "/":

                            pPil2 = 2
                            if pExp > pPil2:
                                pila.append(i)
                                hecho = True
                            else:
                                post = post + str(pila.pop())
                        elif val == "+" or val == "-":
                            pPil2 = 1
                            if pExp > pPil2:
                                pila.append(i)
                                hecho = True
                            else:
                                post = post + str(pila.pop())
                        elif val == "(":
                            pPil2 = 0
                            if pExp > pPil2:
                                pila.append(i)
                                hecho = True
                            else:
                                post = post + str(pila.pop())
                    else:
                        pila.append(i)
                        hecho = True

            elif i == ")":

                while pila[-1] != "(":
                    post = post + str(pila.pop())
                pila.pop()
            elif i==" ":
                kl=""
            else:  # cuando sea un número


                post = post + str(i)






        while pila:
            post = post + str(pila.pop())

        return post

    def valor(self, expresion):
        val = 0
        pila = []
        for i in expresion:
            f = False

            try:
                num = int(i)


                pila.append(i)
                f = True
            except:
                sigue = 0
                kjh = ""
            if f == False:
                sigue = 0
                if listaValores:
                    for j in listaValores:
                        valor = j
                        if valor.nombre == i:
                            numero = valor.valor
                            pila.append(numero)
                            f = True
            if f == False:
                sigue = 0

                num2 = int(pila.pop())
                num1 = int(pila.pop())

                if i == "*":
                    val = num2 * num1
                    pila.append(val)
                elif i == "/":
                    val = num2 / num1
                    pila.append(val)
                elif i == "+":
                    val = num2 + num1
                    pila.append(val)
                elif i == "-":
                    val = num2 - num1
                    pila.append(val)

        return val
