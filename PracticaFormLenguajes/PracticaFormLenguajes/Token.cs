using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PracticaFormLenguajes
{
    class Token
    {
        public enum Tipo {

            Reservado_Planificador,
            Reservado_año,
            Reservado_Mes,
            Reservado_Dia,
            Reservado_Descripcion,
            Reservado_Imagen,
            Cadena,
            Dos_Puntos,
            Número,
            LLave_de_Cierre,
            LLave_de_entrada,
            Desconocido

        }

        private Tipo tipoToken;
        private String valor;
        private int idToken;
        private int fila;
        private int columna;


        public Token(Tipo tipoDelToken, String val,int idToken,int fila,int columna) {//CONTSTRUCTOR DE MI TOKEN CON TODAS SUS CARACTERISTICAS

            this.tipoToken = tipoDelToken;
            this.valor = val;
            this.idToken = idToken;
            this.fila = fila;
            this.columna = columna;



        }

        public Token(Tipo tipoDelToken, String val, int fila, int columna) {//CONSTRUCTO DE MI TOKEN DE ERRORES

            this.tipoToken = tipoDelToken;
            this.valor = val;
            this.idToken = 0;
            this.fila = fila;
            this.columna = columna;

        }

        public String Getval() {
            return valor;
        }

        public int GetidToken()
        {
            return idToken;
        }

        public int Getifila()
        {
            return fila;
        }

        public int Getcolumna()
        {
            return columna;
        }



        public String GetTipo() {
            switch (tipoToken) {
                case Tipo.Cadena:
                    return "Cadena";
                case Tipo.Dos_Puntos:
                    return "Dos Puntos";
                case Tipo.LLave_de_Cierre:
                    return "Llave de Cierre";
                case Tipo.LLave_de_entrada:
                    return "LLave de entrada";
                case Tipo.Número:
                    return "Número";
                case Tipo.Reservado_año:
                    return "Reservado año";
                case Tipo.Reservado_Descripcion:
                    return "Reservado Descripción";
                case Tipo.Reservado_Dia:
                    return "Reservado Dia";
                case Tipo.Reservado_Imagen:
                    return "Reservado Imagen";
                case Tipo.Reservado_Planificador:
                    return "Reservado Planificador";
                case Tipo.Reservado_Mes:
                    return "Reservado Mes";
                default:
                    return "DESCONOCIDO";
            }
        }

    }


}
