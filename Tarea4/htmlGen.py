import webbrowser
def html_create(lista):
    template = open("plantillahtml/template.html","r")
    output = open("reporteTarea4.html","w")

    print(len(lista))
    i=0
    while i< len(lista):
        text = template.read().format(get_num="0", get_nombre="", get_edad="", get_activo="", get_promedio="")
        output.write(text)

        output.writelines("<tr>")
        output.writelines("<th scope = 'row'>%s</th >" % (i + 1))

        output.writelines("<td> %s </td>" % lista[i].getNombre())
        output.writelines("<td> %s </td>" % lista[i].getEdad())
        output.writelines("<td> %s </td>" % lista[i].getActivo())
        output.writelines("<td> %s </td>" % lista[i].getSaldo())
        output.writelines("</tr>")

        i += 1
    output.writelines(" </tbody>")
    output.writelines(" </table>")
    output.writelines(" </html>")
    template.close()
    output.close()

    webbrowser.open_new_tab('reporteTarea4.html')