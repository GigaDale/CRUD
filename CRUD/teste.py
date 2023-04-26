import requests
from bs4 import BeautifulSoup

link = "https://www.google.com/search?client=opera-gx&q=cotação+dolar"

requisicao = requests.get(link)
print(requisicao)
# print(requisicao.text)
site = BeautifulSoup(requisicao.text, "html.parser")
# print(site.prettify())
print(site.find)