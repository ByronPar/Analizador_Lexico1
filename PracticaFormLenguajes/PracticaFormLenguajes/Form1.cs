using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Collections;
using System.IO;
using System.Diagnostics;

namespace PracticaFormLenguajes
{
    public partial class Form1 : Form
    {

        ArrayList ListaPestaña = new ArrayList();
        ArrayList ListaCaja = new ArrayList();

        int contarpestaña = 1;

        public Form1()
        {


            InitializeComponent();
            this.CenterToScreen();
            this.Text = "Analizador Lexico - Practica 1";
           // textBox2.Text = "4.124*(5+6.1781*(8/2^3)-7)-1";


        }

        private void CrearPestaña() {
            TabPage NuevaPestaña = new TabPage("Pestaña  " + contarpestaña);
            TextBox nuevoCaja = new TextBox();
            nuevoCaja.Multiline = true;
            nuevoCaja.Location = new Point(5,5);
            nuevoCaja.ScrollBars = ScrollBars.Vertical;
            nuevoCaja.AcceptsReturn = true;
            nuevoCaja.AcceptsTab = false;
            nuevoCaja.WordWrap = true;
            nuevoCaja.Height = 440;
            nuevoCaja.Width = 380;

            NuevaPestaña.Controls.Add(nuevoCaja);
            

            ListaPestaña.Add(NuevaPestaña);
            ListaCaja.Add(nuevoCaja);




            tabControl1.TabPages.Add(NuevaPestaña);

            contarpestaña++;
            tabControl1.SelectedTab = NuevaPestaña;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        //    monthCalendar1.BoldedDates = new DateTime[] {
        //       new DateTime(12,12, 12),
        //       new DateTime(2019,12, 12),
        //};



        }



        private void Button1_Click_1(object sender, EventArgs e)
        {
            if (contarpestaña == 1)
            {
                MessageBox.Show("Debe Crear una Pestaña para Empezar");
            }
            else
            {
                monthCalendar1.RemoveAllBoldedDates();
                textBox1.Clear();
                int a = 0;
                int s = 0;
                String entrada = "";
                foreach (Control ctrl in tabControl1.SelectedTab.Controls)
                {
                    if (ctrl is TextBox)
                    {
                        //Si entra, es que se tiene un textbox

                        entrada = ctrl.Text;

                    }
                }

                // String entrada= textBox2.Text;
                AnalizadorLexico lex = new AnalizadorLexico();
                LinkedList<Token> lTokens = lex.escanear(entrada);
                lex.imprimirListaToken(lTokens);

                //METODOS PARA GENERAR MI TREEVIEW
                treeView1.Nodes.Clear();               //limpio mi arbol

                foreach (Token item in lTokens) // para crear un mi vector de mis tokens
                {
                    a++;

                }

                Token[] arregloTokens = new Token[a];


                foreach (Token item in lTokens) // lleno mi vector de todos mis tokens
                {
                    arregloTokens[s] = item;
                    s++;

                }


                //AHORA QUE TENGO MI VECTOR DE TOKENS

                int estado = 0;
                int jerar1 = 0;
                int jerar2 = 0;
                int jerar3 = 0;
                int jerar4 = 0;
                int anioC = 0;
                int mesC = 0;
                int diaC ;
                String datosTag = "";
                String dia = "";


                for (int i = 0; i < arregloTokens.Length; i++)
                {

                    switch (estado)
                    {
                        case 0:
                            if (arregloTokens[i].GetTipo().Equals("Reservado Planificador", StringComparison.InvariantCultureIgnoreCase))
                            {
                                estado = 1;
                                jerar2 = 0;
                                jerar3 = 0;
                                jerar4 = 0;
                            }
                            break;
                        case 1:
                            if (arregloTokens[i].GetTipo().Equals("Cadena", StringComparison.InvariantCultureIgnoreCase))
                            {
                                //tomola cadena y coloco en el arbol como un nodo
                                String nombrePlan = arregloTokens[i].Getval();
                                nombrePlan.ToString().Replace('"', ' ').Trim();

                                treeView1.Nodes.Add(nombrePlan);
                                jerar1++;
                                jerar2 = 0;
                                jerar3 = 0;
                                jerar4 = 0;

                                estado = 2;

                            }

                            break;
                        case 2:
                            if (arregloTokens[i].GetTipo().Equals("Reservado año", StringComparison.InvariantCultureIgnoreCase))
                            {
                                estado = 3;

                            }

                            break;
                        case 3:
                            if (arregloTokens[i].GetTipo().Equals("Número", StringComparison.InvariantCultureIgnoreCase))
                            {

                                //tomo el numero
                                String anio = arregloTokens[i].Getval().Trim();
                                treeView1.Nodes[jerar1-1].Nodes.Add(anio);
                                jerar2++;
                                jerar3 = 0;
                                jerar4 = 0;
                                anioC = Int32.Parse(anio); 
                                estado = 4;

                            }

                            break;
                        case 4:
                            if (arregloTokens[i].GetTipo().Equals("Reservado Mes", StringComparison.InvariantCultureIgnoreCase))
                            {

                                estado = 5;

                            }

                            break;
                        case 5:
                            if (arregloTokens[i].GetTipo().Equals("Número", StringComparison.InvariantCultureIgnoreCase))
                            {
                                //tomo el numero
                                String mes = arregloTokens[i].Getval().Trim();
                                treeView1.Nodes[jerar1-1].Nodes[jerar2-1].Nodes.Add(mes);
                                jerar3++;
                                jerar4 = 0;
                                mesC = Int32.Parse(mes);
                                estado = 6;

                            }
                            break;
                        case 6:
                            if (arregloTokens[i].GetTipo().Equals("Reservado Dia", StringComparison.InvariantCultureIgnoreCase))
                            {

                                estado = 7;

                            }
                            break;
                        case 7:
                            if (arregloTokens[i].GetTipo().Equals("Número", StringComparison.InvariantCultureIgnoreCase))
                            {
                                //tomo el número
                                 dia = arregloTokens[i].Getval().Trim();
                               // treeView1.Nodes[jerar1 - 1].Nodes[jerar2 - 1].Nodes[jerar3 - 1].Nodes.Add(dia);
                                jerar4++;
                                diaC = Int32.Parse(dia);

                                
                                    DateTime negrita = new DateTime(anioC, mesC, diaC);
                                    monthCalendar1.AddBoldedDate(negrita);
                                

                                
                                estado = 8;

                               



                            }
                            break;
                        case 8:
                            if (arregloTokens[i].GetTipo().Equals("Reservado Descripción", StringComparison.InvariantCultureIgnoreCase))
                            {

                                estado = 9;

                            }
                            break;
                        case 9:
                            if (arregloTokens[i].GetTipo().Equals("Cadena", StringComparison.InvariantCultureIgnoreCase))
                            {
                                datosTag += arregloTokens[i].Getval().Trim() ;
                                estado = 10;

                            }
                            break;
                        case 10:
                            if (arregloTokens[i].GetTipo().Equals("Reservado Imagen", StringComparison.InvariantCultureIgnoreCase))
                            {

                                estado = 11;

                            }
                            break;
                        case 11:
                            if (arregloTokens[i].GetTipo().Equals("Cadena", StringComparison.InvariantCultureIgnoreCase))
                            {
                                //tomo la cadena

                                datosTag +="-"+arregloTokens[i].Getval().Trim();
                                treeView1.Nodes[jerar1 - 1].Nodes[jerar2 - 1].Nodes[jerar3 - 1].Nodes.Add(dia.Trim()).Tag=datosTag.Trim();
                                datosTag = "";
                                for (int j = i; j < arregloTokens.Length; j++) 
                                {
                                    if (arregloTokens[j].GetTipo().Equals("Reservado Dia", StringComparison.InvariantCultureIgnoreCase))
                                    {
                                        diaC = 0;
                                        estado = 6;
                                        break;

                                    }
                                    else if (arregloTokens[j].GetTipo().Equals("Reservado Mes", StringComparison.InvariantCultureIgnoreCase))
                                    {
                                        diaC = 0;
                                        mesC = 0;
                                        estado = 4;
                                        break;
                                    }
                                    else if (arregloTokens[j].GetTipo().Equals("Reservado año", StringComparison.InvariantCultureIgnoreCase))
                                    {
                                        diaC = 0;
                                        mesC = 0;
                                        anioC = 0;
                                        estado = 2;
                                        break;
                                    }
                                    else if (arregloTokens[j].GetTipo().Equals("Reservado Planificador", StringComparison.InvariantCultureIgnoreCase))
                                    {
                                        estado = 0;
                                        break;
                                    }
                                }



                            }

                            break;
                        default:

                            //nada
                            break;

                    }

                }

                //CONTINUAR CON LA FUNCIONALIDAD DE GENERAR EL HTML 
                //dos variables para ver si existen token de errores o verdaderos
                int token=0;
                int tokenError=0;

                for (int i = 0; i < arregloTokens.Length; i++)
                {
                    if (arregloTokens[i].GetTipo().Equals("Reservado Imagen", StringComparison.InvariantCultureIgnoreCase) ||
                        arregloTokens[i].GetTipo().Equals("Cadena", StringComparison.InvariantCultureIgnoreCase) ||
                        arregloTokens[i].GetTipo().Equals("Dos Puntos", StringComparison.InvariantCultureIgnoreCase) ||
                        arregloTokens[i].GetTipo().Equals("Llave de Cierre", StringComparison.InvariantCultureIgnoreCase) ||
                        arregloTokens[i].GetTipo().Equals("LLave de entrada", StringComparison.InvariantCultureIgnoreCase) ||
                        arregloTokens[i].GetTipo().Equals("Número", StringComparison.InvariantCultureIgnoreCase) ||
                        arregloTokens[i].GetTipo().Equals("Reservado año", StringComparison.InvariantCultureIgnoreCase) ||
                        arregloTokens[i].GetTipo().Equals("Reservado Descripción", StringComparison.InvariantCultureIgnoreCase) ||
                        arregloTokens[i].GetTipo().Equals("Reservado Dia", StringComparison.InvariantCultureIgnoreCase) ||
                        arregloTokens[i].GetTipo().Equals("Reservado Mes", StringComparison.InvariantCultureIgnoreCase))
                    {
                        token = 1;
                    }
                    else if (arregloTokens[i].GetTipo().Equals("DESCONOCIDO", StringComparison.InvariantCultureIgnoreCase))
                    {
                        tokenError = 1;
                    }
                   
                }

                int contadorToken = 0;
                if (token==1) //SI HAY TOKEN VERDADEROS SE CREARA UN ARCHIVO HTML CON LOS TOKEN VALIDOS,
                {
                    StreamWriter html1 = new StreamWriter("C:\\Users\\HP ENVY\\Desktop\\TablaTokens.html");
                    html1.WriteLine("<html><h1><center>Tabla De Tokens</center></h1>"
                        + "<br>"
                        + "<center>No ------------------------------- TIPO ------------------------------- VALOR ------------------------------- ID TOKEN ------------------------------- FILA ------------------------------- COLUMNA</center>");
                    html1.WriteLine("<center><table border = '1'>");
                    for (int i = 0; i < arregloTokens.Length; i++)
                    {

                        if (arregloTokens[i].GetTipo().Equals("DESCONOCIDO", StringComparison.InvariantCultureIgnoreCase))
                        {
                           //nada
                        }
                        else {
                            contadorToken++;
                            html1.WriteLine(" <tr>"
                                + " <td WIDTH=160 bgcolor=green>" + contadorToken + "</td><td WIDTH=200 bgcolor=green>" + arregloTokens[i].GetTipo() + "</td>"
                                + " <td WIDTH=280 bgcolor=green>" + arregloTokens[i].Getval() + "</td><td WIDTH=250 bgcolor=green>" + arregloTokens[i].GetidToken() + "</td>"
                                + " <td WIDTH=230 bgcolor=green>" + arregloTokens[i].Getifila() + "</td><td WIDTH=150 bgcolor=green>" + arregloTokens[i].Getcolumna() + "</td>"
                                + "   </tr>");
                        }

                       
                    }

                    html1.WriteLine(" </table></center>"
                    + "</body>"
                    + "</html>");
                    html1.Close();
                }

                contadorToken = 0;
                if (tokenError==1) //SI HAY TOKEN FALSOS SE CREARA UN ARCHIVO HTML CON LOS TOKEN DE ERRORES
                {
                    StreamWriter html2 = new StreamWriter("C:\\Users\\HP ENVY\\Desktop\\TablaTokensDeErrores.html");
                    html2.WriteLine("<html><h1><center>Tabla De Tokens de Errores</center></h1>"
                        + "<br>"
                        + "<center>No ------------------------------- TIPO ------------------------------- VALOR ------------------------------- ID TOKEN ------------------------------- FILA ------------------------------- COLUMNA</center>");
                    html2.WriteLine("<center><table border = '1'>");
                    for (int i = 0; i < arregloTokens.Length; i++)
                    {

                        if (arregloTokens[i].GetTipo().Equals("DESCONOCIDO", StringComparison.InvariantCultureIgnoreCase))
                        {
                            contadorToken++;
                            html2.WriteLine(" <tr>"
                                + " <td WIDTH=160 bgcolor=green>" + contadorToken + "</td><td WIDTH=200 bgcolor=green>" + arregloTokens[i].GetTipo() + "</td>"
                                + " <td WIDTH=280 bgcolor=green>" + arregloTokens[i].Getval() + "</td><td WIDTH=250 bgcolor=green>" + arregloTokens[i].GetidToken() + "</td>"
                                + " <td WIDTH=230 bgcolor=green>" + arregloTokens[i].Getifila() + "</td><td WIDTH=150 bgcolor=green>" + arregloTokens[i].Getcolumna() + "</td>"
                                + "   </tr>");
                        }
                        else
                        {
                            
                        }


                    }

                    html2.WriteLine(" </table></center>"
                    + "</body>"
                    + "</html>");
                    html2.Close();
                }

                   



            }
        }

        private void ComboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void SalirToolStripMenuItem_Click_1(object sender, EventArgs e)
        {
            //System.exit(0);
            Application.Exit();
        }

        private void NuevaPestañaToolStripMenuItem_Click(object sender, EventArgs e)
        {
            CrearPestaña();
        }

        private void CargarArchivpToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (contarpestaña == 1)
            {
                MessageBox.Show("Debe Crear una Pestaña para Empezar");
            }
            else
            {
                //CONTINUAR AQUI DESPUES DE CENAR XD
                OpenFileDialog ventana = new OpenFileDialog();
                ventana.Filter = "Archivos ly(*.ly)|*.ly";
                ventana.Title = "Archivos ly";
                ventana.FileName = "Sin titulo... ";

                if (ventana.ShowDialog() == DialogResult.OK)
                {
                    //AQUI DEBO COLOCAR LA FUNCIONALIDAD PARA OBTENER EL TEXTO
                    StreamReader leer = new StreamReader(ventana.FileName);
                    

                    foreach (Control ctrl in tabControl1.SelectedTab.Controls) { 
                        if (ctrl is TextBox) {
                            //Si entra, es que se tiene un textbox

                            ctrl.Text = leer.ReadToEnd();
                            leer.Close();
                        }
                    }







                }
            }



        }

        private void MonthCalendar1_DateChanged(object sender, DateRangeEventArgs e)
        {

        }

        private void MenuStrip1_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {
            
        }

        private void TreeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {

            try {
                pictureBox1.Image = null;
                textBox1.Text = "";
                //creo dos string uno donde estara mi ruta de imagen y la otra esta mi descripción
                String[] datos = e.Node.Tag.ToString().Split('-');
                String ruta = datos[1].Trim();
                String des = datos[0].Trim();

                textBox1.Text = des;
                pictureBox1.Image = Image.FromFile(ruta);
                pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;

                //MessageBox.Show(e.Node.Text);
                // MessageBox.Show(e.Node.Tag.ToString());

            }
            catch (Exception al) {
                //nada
            }
            
            


        }

        private void ManualAplicaciónToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Process.Start("C:/Users/HP ENVY/Desktop/ManualDeUsuarioAnalizadoLexico.pdf");
            
        }

        private void AcercaDeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Programa Realizado por:      Byron Josué Par Rancho" +
                "\n\n" +
                "\nCarnet: 201701078" +
                "\n\n" +
                "\nEstudiante de Ingenieria en Ciencias y Sistemas" +
                "\n\n" +
                "\nPractica Número 1 - Lenguajes Formales y de Programación" +
                "\n\n" +
                "\nSección: A+   ");
        }

        private void GuardarToolStripMenuItem_Click(object sender, EventArgs e)
        {

            if (contarpestaña == 1)
            {
                MessageBox.Show("Debe Crear una Pestaña para Empezar");
            }
            else
            {
                foreach (Control ctrl in tabControl1.SelectedTab.Controls)
            {
                if (ctrl is TextBox)
                {
                        //Si entra, es que se tiene un textbox

                        SaveFileDialog guardar = new SaveFileDialog();
                        guardar.InitialDirectory = @"C:\";
                        guardar.RestoreDirectory = true;
                        guardar.FileName = "*.txt";
                        guardar.DefaultExt = "txt";
                        guardar.Filter = "txt files (*.txt)|*.txt";

                        if (guardar.ShowDialog()== DialogResult.OK)
                        {
                            Stream fileStream = guardar.OpenFile();
                            StreamWriter algo = new StreamWriter(fileStream);
                            algo.Write(ctrl.Text);
                            algo.Close();
                            fileStream.Close();

                        }

                }
            }
        }
        }
    }
}
