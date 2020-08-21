import csv

def  cargar_datosCSV(ruta):
   with open(ruta) as cont:
      archivocsv = csv.reader(cont)
      encabezado = next(archivocsv)
      print("******------DATOS EN CSV-------*****")
      print(encabezado)
      print()
      for registro in archivocsv:
          print(registro)
      print("La clase de la estructura es: ")
      print(type(archivocsv))
      print("******------FIN DE DATOS EN CSV-------*****")