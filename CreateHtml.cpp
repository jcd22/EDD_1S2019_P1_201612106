#include <iostream>
#include <iostream>
#include <windows.h>
#include <string>
#include <fstream>
#include <conio.h>
#include <sstream>
#include <cstdlib>
#include <vector>
//nueva linea

using namespace std;

class createHtml{

private:
    int x;
    int y;

public:
    createHtml(int x, int y){
    this->x = x;
    this->y = y;

    }

    void InsertHtml() {
            string jsContent = "";
            string ruta = "";
            string posicion = "";
            string color = "";

			// Obtener Nombre De Archivo Inicial
			cout << "\nEnter Initial File Name -> ";
			cin >> ruta; // Ingresar Nombre De Archivo
			ruta =  ruta + ".js"; // Agregar Extensión
			ofstream fs("HtmlMatrix.html");
			 // ofstream file;
              //file.open("C:/ruta/archivos/archivo.txt");
            jsContent = jsContent + "<!DOCTYPE html>  \n"
                                      + "<html>  \n"
                                      + "<title>Juan Pixel Art</title> \n"
                                      + "<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js\"></script> \n"
                                      + "<link rel=\"stylesheet\" href=\"PixelArt.css\">"
                                      + "</head> \n"
                                      + "<body> \n"
                                      + "<div  id=\"bodyart\" class=\"bodyart\"> \n";

            for(int i= x; i >= 1 ;i--){
                for(int j = 1; j<= y; j++){

                        stringstream ss;
                        stringstream sss;

                        ss << i ;
                        sss<< j ;

                        string si = ss.str();
                        string sj = sss.str();
                   jsContent = jsContent +  "<div id =\"a"+si+"-"+sj+"\"></div> \n";
                }

            }

            jsContent = jsContent + "</div> \n"
                                      + "</body> \n"
                                      + "</html> \n";
              fs << jsContent;
              fs.close();


}
};

class createCss{
private:
public:
    createCss(int x ,int y, string color )
    {
            string cssContent = "";
            string corX = "";
            string corY= "";
            string ruta;

            //para ls colores dividimos con arreglo

vector<string> pablo;
size_t found;
size_t found2;
string linea = "Roberto,Giordano";
found = linea.find(",");
string linea2 = linea.substr(found+1,linea.size());
found2 = linea2.find(",");
pablo.push_back(linea.substr(0,found));
pablo.push_back(linea2.substr(0,found2));
pablo.push_back(linea2.substr(found2+1,linea2.size()));



cout<<pablo[0]<<"\n"<<pablo[1]<<"\n"<<pablo[2]<<endl;


			// Obtener Nombre De Archivo Inicial
			cout << "\nEnter Initial File Name -> ";
			cin >> ruta; // Ingresar Nombre De Archivo
			ruta =  ruta + ".css"; // Agregar Extensión
			ofstream fs("HtmlMatrix.css");
			 // ofstream file;
              //file.open("C:/ruta/archivos/archivo.txt");
            cssContent = cssContent + "body { background: #FFF; margin: 0; padding: 0; }"
+" #bodyart{ margin:0; padding: 0; background: #666; width: 480px; height: 480px; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);}"
+" #bodyart div { margin: 0; padding: 0; background: #FFF; width: 30px; height: 30px; border: 1px solid #666; display: block; float: left; box-sizing: border-box; text-align: center; line-height: 25px; font-size: 12px; };";

            for(int i= 1; i <= x ;i++){
                for(int j = 1; j<= y; j++){
                        stringstream ss;
                        stringstream sss;

                        ss << i ;
                        sss<< j ;

                        string si = ss.str();
                        string sj = sss.str();



                        cssContent = cssContent + "#bodyart #a"+si+"-"+sj+"{ background-color:"+color+"; };";

                }

            }
                        cssContent = cssContent + "#bodyart div{ background-color: black;}";

              fs << cssContent;
              fs.close();

    }

};

int main(){

    createHtml *newHtml = new createHtml(16,16);
    newHtml->InsertHtml();


    return 0;

    }
