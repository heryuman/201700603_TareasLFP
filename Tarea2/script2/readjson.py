import json
def  cargar_datos(ruta):
   with open(ruta) as cont:
      archivo = json.load(cont)
      print("******------DATOS EN JSON--------*****")
      for archivo in archivo:
       print(archivo.get('nombre')+ " "+archivo.get('Apellido'))
      print("La clase de la estructura es: ")
      print(type(archivo))
      print("******------ FIN DE DATOS EN JSON-------*****")