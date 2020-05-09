using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace PracticaFormLenguajes
{
    class AnalizadorLexico
    {
        private LinkedList<Token> Salida;
        private int estado;
        private String auxlex;
        private int columna;
        private int fila;
        

        public LinkedList<Token> escanear(String entrada)
        {

            entrada = entrada + "#";
            Salida = new LinkedList<Token>();
            estado = 0;
            auxlex = "";
            Char c;
            fila = 1;
            columna = 1;


            for (int i = 0; i <= entrada.Length-1; i++)
            {
                c = entrada.ElementAt(i);
                switch (estado)
                {
                    case 0:
                        if (Char.IsDigit(c))
                        {
                            estado = 2;

                            auxlex += c;
                            columna++;

                        }
                        else if (c.CompareTo('"') == 0)
                        {
                            estado = 5;

                            //auxlex += c;
                            columna++;


                        }
                        else if (c.CompareTo(':') == 0)
                        {
                            auxlex += c;
                            agregarToken(Token.Tipo.Dos_Puntos,4);

                            columna++;

                        }
                        else if (c.CompareTo('{') == 0)
                        {
                            
                            auxlex += c;
                            agregarToken(Token.Tipo.LLave_de_entrada, 4);

                            columna++;

                        }
                        else if (c.CompareTo('}') == 0)
                        {
                            
                            auxlex += c;
                            agregarToken(Token.Tipo.LLave_de_Cierre, 4);
                            columna++;

                        }
                        else if ((((int)(c) >= 65) && ((int)(c) <= 90)) || (((int)(c) >= 97) && ((int)(c) <= 122)))
                        {
                            estado = 1;
                            auxlex += c;
                            columna++;


                        }
                        else if (c== ' ')
                        {
                            auxlex += "+ Espacio en blanco";
                            agregarTokenError(Token.Tipo.Desconocido);
                            columna++;
                        }
                        else if (c.CompareTo('\n')==0 )
                        {
                            auxlex +="+ Salto de linea";
                            agregarTokenError(Token.Tipo.Desconocido);
                            columna = 1;
                            fila++;
                        }
                        else
                        {

                            if (c.CompareTo('#') == 0 && i == entrada.Length - 1)
                            {
                                Console.WriteLine("Hemos concluido el analisis con exito");
                            }
                            else
                            {                              // AQUI EJECUTARE MI METODO PARA AGREGAR MI ERROR, A MI LISTA DE TOKENS DE ERROES    

                                if (c.CompareTo('\r') == 0)
                                {
                                    
                                }
                                else if (c.CompareTo('\t') == 0)
                                {
                                   
                                }
                                else if (c.CompareTo('\f') == 0)
                                {
                                   
                                }
                                else if (c.CompareTo('\b') == 0)
                                {
                              
                                }
                                else
                                {

                                    auxlex += c;
                                    agregarTokenError(Token.Tipo.Desconocido);
                                    columna++;

                                }


                                
                            }
                        }

                        break;
                    case 1:                              //COMPRUEBO QUE MI STRING AUXLEX NO SEA IGUAL A NINGUNA PALABRA RESERVADA , DE LO CONTRARIO AGREGO MI TOKEN
                        if (auxlex.Equals("Planificador",StringComparison.InvariantCultureIgnoreCase))
                        {
                            agregarToken(Token.Tipo.Reservado_Planificador,1);
                            columna++;
                            i -= 1;

                        }else if (auxlex.Equals("Anio", StringComparison.InvariantCultureIgnoreCase))
                        {
                            agregarToken(Token.Tipo.Reservado_año, 1);
                            columna++;
                            i -= 1;
                        }
                        else if (auxlex.Equals("Mes", StringComparison.InvariantCultureIgnoreCase))
                        {
                            agregarToken(Token.Tipo.Reservado_Mes, 1);
                            columna++;
                            i -= 1;
                        }
                        else if (auxlex.Equals("Dia", StringComparison.InvariantCultureIgnoreCase))
                        {
                            agregarToken(Token.Tipo.Reservado_Dia, 1);
                            columna++;
                            i -= 1;
                        }
                        else if (auxlex.Equals("Descripcion", StringComparison.InvariantCultureIgnoreCase))
                        {
                            agregarToken(Token.Tipo.Reservado_Descripcion, 1);
                            columna++;
                            i -= 1;
                        }
                        else if (auxlex.Equals("Imagen", StringComparison.InvariantCultureIgnoreCase))
                        {
                            agregarToken(Token.Tipo.Reservado_Imagen, 1);
                            columna++;
                            i -= 1;
                        }
                        else  if ((((int)(c) >= 65) && ((int)(c) <= 90)) || (((int)(c) >= 97) && ((int)(c) <= 122)))//SI NO ES NINGUNA PALABRA AUN , SIGO VERIFICANDO EL SIGUIENTE CARACTER

                        {
                            estado = 1;
                            auxlex += c;
                            columna++;

                        }else if (c.CompareTo('\n') == 0 )
                        {
                            auxlex += "+ Salto de linea ";
                            agregarTokenError(Token.Tipo.Desconocido);
                            columna = 1;
                            fila++;
                        }
                        else {
                            agregarTokenError(Token.Tipo.Desconocido);
                           
                            i -= 1;
                        }
                        
                        break;
                    case 2:
                        if (Char.IsDigit(c))
                        {
                            estado = 2;
                            auxlex += c;
                            columna++;
                        }
                        else if (c.CompareTo('.') == 0)
                        {
                            estado = 3;
                            auxlex += c;
                            columna++;
                        }
                        else if (c.CompareTo('\n') == 0  )
                        {
                            auxlex += "+ Salto ";
                            agregarToken(Token.Tipo.Número,3);
                            columna = 1;
                            fila++;
                        }
                        else {

                            agregarToken(Token.Tipo.Número,3);
                            i -= 1;
                            columna++;
                        }
                        break;
                    case 3:
                        if (Char.IsDigit(c))
                        {
                            estado = 4;
                            auxlex += c;
                            columna++;
                        }
                        else if (c.CompareTo('\n') == 0)
                        {
                            auxlex += "+ Salto ";
                            agregarToken(Token.Tipo.Número, 3);
                            columna = 1;
                            fila++;
                        }
                        else {
                            agregarToken(Token.Tipo.Número,3);
                            i -= 1;
                        }
                        break;
                    case 4:                                    // SIGNO MAS
                        if (Char.IsDigit(c))
                        {
                            estado = 4;
                            auxlex += c;
                            columna++;
                        }
                        else if (c.CompareTo('\n') == 0 )
                        {
                            auxlex += "+ Salto ";
                            agregarToken(Token.Tipo.Número, 3);
                            columna = 1;
                            fila++;
                        }
                        else
                        {
                            agregarToken(Token.Tipo.Número, 3);
                            i -= 1;
                        }
                        break;
                    case 5:                                  
                        if (c.CompareTo('"') == 0)
                        {
                            //auxlex += c;
                            columna++;
                            agregarToken(Token.Tipo.Cadena,2);
                            columna++;

                        }
                        else if (c.CompareTo('\n') == 0 || c.CompareTo('\r') == 0 || c.CompareTo('\t') == 0 || c.CompareTo('\f') == 0 || c.CompareTo('\b') == 0)
                        {
                            estado = 5;
                            columna = 1;
                            fila++;
                        }
                        else  if (c.CompareTo('#') == 0 && i == entrada.Length - 1)
                        {
                            
                            //auxlex += c;
                            columna++;
                            agregarTokenError(Token.Tipo.Desconocido);
                            columna++;
                        }
                        else
                        {
                            estado = 5;
                            auxlex += c;
                            columna++;
                        }
                        break;
                    
                }

            }
            return Salida;


        }

        public void agregarToken(Token.Tipo tipo,int idToken)
        {
            Salida.AddLast(new Token(tipo, auxlex, idToken, fila, columna));
            auxlex = "";
            estado = 0;
        }

        public void agregarTokenError(Token.Tipo tipo) {
            Salida.AddLast(new Token(tipo, auxlex, fila, columna));
            auxlex = "";
            estado = 0;

        }

        public void imprimirListaToken(LinkedList<Token> lista)
        {
            int a = 0;
            foreach (Token item in lista)
            {
                Console.WriteLine(item.GetTipo() + "  <-->  " + item.Getval() + "  <-->  " + item.Getifila() + "  <-->  " + item.Getcolumna() + "  <-->  " + item.GetidToken());

            }




        }





    }


}

