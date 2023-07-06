import requests
import pandas
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000/'
#obtengo la página ha analizar
html_doc = requests.get(url)
#print(html_doc.text)
#parsear la página web
soup = BeautifulSoup(html_doc.text, 'html.parser')

#txt_html = html_doc.text
#titulo = txt_html.startswith("<title>")
#print(titulo)

#print(soup.prettify())
#titulo = soup.title

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)

print(soup.p)

titulo_datos = soup.h1.string
print(titulo_datos)

#tabla = soup.find('table')

#obtener las filas de la tabla
#filas = tabla.find_all('tr')

#Iterar sobre las filas e imprimir los datos
#for fila in filas:
    #Obtener las celdas de la fila
    #celdas = fila.find_all('td')

    #Extraer los datos de las celdas
    #datos = [celda.get_text(strip=True) for celda in celdas]

    #Imprimir los datos
    #print(datos)

tabla = soup.find('table')

#obtener las filas de la tabla
filas = tabla.find_all('tr')

nombres = []
apellidos = []
emails = []

#Iterar sobre las filas e imprimir los datos
for fila in filas:
    #Obtener las celdas de la fila
    celdas = fila.find_all('td')
    if len(celdas)>0:
    #print(celdas)
    #print(celdas[0])
        #print(celdas[1].string)
        nombres.append(celdas[1].string)
        #print(celdas[2])
        apellidos.append(celdas[2].string)
        #print(celdas[3])
        #print(celdas[4])
        emails.append(celdas[4].string)

print(nombres)
print(apellidos)
print(emails)

df = pandas.DataFrame({'Nombres':nombres,'Apellidos':apellidos,'Emails':emails})
df.to_csv('personas.csv', index=False, encoding='utf-8')
#df.to_excel('personas.xlsx')