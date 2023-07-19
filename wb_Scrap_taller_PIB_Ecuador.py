import re

import requests
import pandas as pd
from bs4 import BeautifulSoup

fecha_list = []
pib_euro_list = []
pib_dol_list = []
variacion_list = []

url = 'https://datosmacro.expansion.com/pib/ecuador'
#obtengo la página ha analizar
html_doc = requests.get(url)
soup = BeautifulSoup(html_doc.text, 'html.parser')

tabla =soup.find('table', attrs={'class':"table tabledat table-striped table-condensed table-hover"})

filas = tabla.find_all('tr')
for fila in filas:
    celdas = fila.find_all('td')
    if len(celdas) > 0:
        fecha = celdas[0].string
        pib_euro = re.sub(r'[^\d.]', '', str(celdas[1].string))
        pib_dol = re.sub(r'[^\d.]','', celdas[2].string)
        variacion = celdas[3].string
        fecha_list.append(fecha)
        pib_euro_list.append(pib_euro)
        pib_dol_list.append(pib_dol)
        variacion_list.append(variacion)

#print(fecha_list)
#print(pib_euro_list)
#print(pib_dol_list)
#print(variacion_list)

df = pd.DataFrame({'Año':fecha_list, 'PIB (Euros)':pib_euro_list, 'PIB (Dolares)':pib_dol_list, 'Variacion':variacion_list})
df.to_csv('PIB_Ecuador.csv', index=False, encoding='utf-8')

