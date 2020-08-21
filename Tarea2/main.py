
from script2 import  readxml
from script2 import  readjson
from script2 import  readcsv

if __name__ == '__main__':
   ruta ='datos/archivosJ.json'
   ruta2='datos/archxml.xml'
   ruta3='datos/archcsv.csv'
   readjson.cargar_datos(ruta)
   readxml.cargar_XML(ruta2)
   readcsv.cargar_datosCSV(ruta3)
