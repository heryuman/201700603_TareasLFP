def lector(entrada):
    print("Cadena a leer: ",entrada)
    caracteres= list(entrada + "#")
    estado=0
   # print(caracteres)
    i=0
    while  i < len(caracteres):
        #print(caracteres[i])
       # print("estado:",estado)

        if estado == 0:

            if caracteres[i].isalpha():
              #  print("el caracter leido: ",caracteres[i])
                estado = 2


            elif caracteres[i] == "_":
               # print("el caracter leido: ", caracteres[i])
                estado = 1


            elif caracteres[i] == "#" and (len(caracteres) - 1):
                 print("Analisis completado con exito")

            else:
                print("caracter incorrecto, cadena invalida")
                break

        elif estado == 1:
            if caracteres[i].isalpha():
                #print("el caracter leido: ", caracteres[i])
                estado = 3


            elif caracteres[i] == "_":
               # print("el caracter leido: ", caracteres[i])
                estado = 1





        elif estado == 2:
            if caracteres[i].isalpha():
              #  print("el caracter leido: ", caracteres[i])
                estado = 2


            elif caracteres[i].isdigit():
               # print("el caracter leido: ", caracteres[i])
                estado = 4




        elif estado == 3:
            if (caracteres[i]).isdigit():
              #  print("el caracter leido: ", caracteres[i])
                estado = 4


            else:
                print("caracter incorrecto, cadena invalida")
                break



        elif estado == 4:
            print("cadena Valida")
            estado = 0
        i+=1
    print("Fin del Analisis")
    print()



