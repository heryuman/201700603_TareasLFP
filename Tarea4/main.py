import objeto
import htmlGen
listaPersonas = []

def creandoPersonas():

     persona1 = objeto.Persona("Raul",25,True,258.43)
     persona2 = objeto.Persona("Ana", 35, False,222.3)
     persona3 = objeto.Persona("Lorena",22,False,1225.3)
     persona4 = objeto.Persona("Nohelia",20,True,25.3)
     persona5 = objeto.Persona("Sofia",21,False, 435.3)
     persona6 = objeto.Persona("Jorge",28,False,685.00)
     persona7 = objeto.Persona("Rocio",19, True,14.35)
     persona8 = objeto.Persona("Alberto",25,False,1553)
     persona9 = objeto.Persona("Manuel",23,True,874)
     persona10 = objeto.Persona("Carlos",27,False,50)

     global listaPersonas
     listaPersonas.append(persona1)
     listaPersonas.append(persona2)
     listaPersonas.append(persona3)
     listaPersonas.append(persona4)
     listaPersonas.append(persona5)
     listaPersonas.append(persona6)
     listaPersonas.append(persona7)
     listaPersonas.append(persona8)
     listaPersonas.append(persona9)
     listaPersonas.append(persona10)

def imprimirlist():

     htmlGen.html_create(listaPersonas)


if __name__ == '__main__':

    creandoPersonas()
    imprimirlist()
