# -*- coding: utf-8 -*-

from google.colab import drive
from bs4 import BeautifulSoup
import requests
import csv

#URL ONDE ESTA A LISTA DE EMAIL A SEREM EXTRAIDOS
link = 'https://vinirodrigues.github.io/raspagem-emails/'
requisicao = requests.get(link)
#DEVE RETORNAR 200 PARA REQUISÇÃO FUNCIONAR
print(requisicao)
site = BeautifulSoup(requisicao.text, "html.parser")
#INDENTA O HTML PARA MELHOR ANALISE
print(site.prettify())

#LOCALIZA A LISTA PELA TAG
lista = site.find("ul")
print(lista)

#MONTA O GOOGLE DRIVE
drive.mount('/content/drive')

# Analisa a variável 'lista' usando BeautifulSoup
soup = BeautifulSoup(str(lista), 'lxml')

# Extrai os itens da lista <li>
items = [li.text for li in soup.find_all('li')]

# Verifica os itens extraídos
print(items)

# Nome do arquivo CSV a ser criado
csv_file_path = '/content/drive/My Drive/lista.csv'

# Escreve os itens em um arquivo CSV
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)

    # Escreve o cabeçalho (opcional)
    csvwriter.writerow(['Item'])

    # Escreve os itens da lista
    for item in items:
        csvwriter.writerow([item])

print(f"Arquivo CSV criado com sucesso em: {csv_file_path}")

