
import  automata

lista = []

lista.append("__servidor1")
lista.append("3servidor")
lista.append("__a1")
lista.append("abc3")

if __name__ == '__main__':
    i=0

    while i < len(lista):
        automata.lector(lista[i])
        i+=1



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
