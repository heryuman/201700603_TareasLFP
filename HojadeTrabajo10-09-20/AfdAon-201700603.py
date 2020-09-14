

entrada= '(<[atributo_numerico]=45.09,[atributo_cadena] = "hola mundo", [atributo_booleano] = true>, <[atributo_numerico] = 4,[atributo_cadena] = "adios mundo",  [atributo_booleano] = false>,<[atributo_numerico] = -56.4, [atributo_cadena] = "este es otro ejemplo, las cadenas pueden ser muy largas",  [atributo_booleano] = false >)'




tokens=[]
lexema=""






def lector(entrada):
    global lexema

    # print("Cadena a leer: ",entrada)
    car= entrada.replace(" ","")
    caracteres= list(entrada+ "#")
    estado=0
   # print(caracteres)
    i=0
    while  i < len(caracteres):
        print(caracteres[i])
        print("estado:",estado)

        if estado == 0:

            if caracteres[i].isalpha():
                #  print("el caracter leido: ",caracteres[i])
                estado = 1
                lexema += caracteres[i]


            elif caracteres[i].isdigit():
                estado = 2
                print("digitos")
                lexema += caracteres[i]


            elif caracteres[i] == "=":

                lexema += caracteres[i]
                agregarToken("tk_sigIgual", lexema)
                estado = 0
            elif caracteres[i] == "_":

                lexema += caracteres[i]
                print("guion bajo")
                agregarToken("tk_gBajo", lexema)
                estado = 0
            elif caracteres[i] == "(":
                lexema += caracteres[i]
                print("token parentesis")
                agregarToken("tk_parA", lexema)
                estado = 0

            elif caracteres[i] == "-":
                lexema += caracteres[i]
                agregarToken("tk_sMenos", lexema)
                estado = 0
            elif caracteres[i] == "+":
                lexema += caracteres[i]
                agregarToken("tk_sMas", lexema)
                estado = 0
            elif caracteres[i] == ")":
                lexema += caracteres[i]
                agregarToken("tk_parC", lexema)
                estado = 0
            elif caracteres[i] == "[":
                lexema += caracteres[i]
                agregarToken("tk_corA", lexema)
                estado = 0
            elif caracteres[i] == "]":
                lexema += caracteres[i]
                agregarToken("tk_corC", lexema)
                estado = 0
            elif caracteres[i] == "<":
                lexema += caracteres[i]
                agregarToken("tk_menorQ", lexema)
                estado = 0
            elif caracteres[i] == ">":
                lexema += caracteres[i]
                agregarToken("tk_mayorQ", lexema)
                estado = 0
            elif caracteres[i] == ",":
                lexema += caracteres[i]
                agregarToken("tk_coma", lexema)
                estado = 0
            elif caracteres[i] == "\"":
                print("comilla")
                estado = 4





        elif estado == 1:
            if caracteres[i].isalpha():
                # print("el caracter leido: ", caracteres[i])
                estado = 1
                lexema = lexema + caracteres[i]
            else:
                agregarToken("tk_palabra", lexema)
                estado = 0



        elif estado == 2:
            if caracteres[i].isdigit():
                lexema += caracteres[i]
                estado = 2

            elif caracteres[i] == ".":
                lexema += caracteres[i]
                estado = 3
            else:
                agregarToken("tk_digito", lexema)
                estado = 0




        elif estado == 3:
            if (caracteres[i]).isdigit():

                estado = 2


            else:
                print("caracter incorrecto, cadena invalida")
                break



        elif estado == 4:

            if caracteres[i].isalpha():
                lexema += caracteres[i]
                estado = 4

            elif caracteres[i]==" ":
                lexema += caracteres[i]
                estado = 4

            elif caracteres[i] == "@":
                lexema+=caracteres[i]
                estado=4

            elif caracteres[i] == '"':
                estado = 5


        elif estado == 5:

            agregarToken("tk_Cadema",lexema)
            estado=0


        i+=1

    print("Fin del Analisis")
    print()
def agregarToken(tipo, valor):

    global lexema
    global tokens
    TipodeToken=(tipo,valor)
    tokens.append(TipodeToken)

    lexema =""


    #print(tokens)

def imprimirlista():
    i = 0
    while i < len(tokens):
        print(tokens[i])
        i += 1



if __name__ == '__main__':
    lector(entrada)
    imprimirlista()

class TipodeToken:

    def __init__(self, Tipo, valor):

        self.tipo= Tipo
        self.val = valor

    def getTipo(self):
        return self.tipo

    def getvalor(self):

        return self.val


