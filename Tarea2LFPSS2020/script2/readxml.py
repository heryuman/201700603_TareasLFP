import xml.etree.ElementTree as ET

def cargar_XML(ruta):
     archivoxml = ET.parse(ruta)
     raiz= archivoxml.getroot()
     print("--------------DATOS XML-----------")
     print(raiz)

     for hijo in raiz:
        print(hijo)
        for nieto in hijo:
          print(nieto)
          print(nieto.text)
     print("El tipo de Estructura es:")
     print(type(raiz))
     print("------------FIN DATOS XML----------")
     print()