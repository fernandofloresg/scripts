# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 18:28:56 2023

@author: ferna
"""

import requests     #instalar desde el prompt con pip install requests

# Beautifulsoup es un librería que permite analizar y recorrer la información de un archivo que contiene etiquetas,
# las cuales forman un árbol
from bs4 import BeautifulSoup #instalar desde el prompt con pip install bs4

#import lxml        #instalar desde el prompt con pip install lxml
#import texttable as tt     #instalar desde el prompt con pip install texttable

# URL para extraer datos
url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
  
# accedemos al URL 
page = requests.get(url)

#Le indicamos que el texto del objeto "page" es de tipo html
soup = BeautifulSoup(page.text, 'html.parser')

#Creamos una lista vacía para almacenar los datos
data = []
  
# soup.find_all('td') traerá cada 
# elemento en la tabla de la URL que se encuentren entre un tag "td"
# que son los que se usan para crear tablas en HTML

# data_iterator es el iterador de la tabla
data_iterator = iter(soup.find_all('td')) 
  

# Este ciclo seguirá repitiéndose hasta que haya
# datos disponibles en el iterador
while True:
    try:
        pais = next(data_iterator).text
        casos_confirmados = next(data_iterator).text
        muertes = next(data_iterator).text
        region = next(data_iterator).text
  
        data.append((
            pais,
            int(casos_confirmados.replace(',', '')),
            int(muertes.replace(',', '')),
            region
        ))
  
    # El error StopIteration se genera cuando
    # no quedan más elementos para
    # iterar
    except StopIteration:
        break
    
print(data)