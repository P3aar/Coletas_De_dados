import requests
from bs4 import BeautifulSoup

url = 'https://wiki.python.org/moin/BeginnersGuide/Programmers'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

#Exibir o texto
print(extracao.text.strip()) #() vazio, remove espacos em branco!

# Filtrar a exibicao pela tag
for linha_texto in extracao.find_all('h2'): #h2 sao Titulos de sites, Utilize inspecionar do site!
    titulo = linha_texto.text.strip()
    print('Titulo: ', titulo)
 #CTRL + Barra = tira o '#' Comentario e transforma em linha de codigo!

'''
desafio
Filtrar ta ['h2','p']
Contar quantos h2 e p existem no documento (linha_texto.name == tag)
'''

# contar qtd de titulos e paragrafos
# contar_titulos = 0
# contar_paragrafos = 0
# 
for linha_texto in extracao.find_all(['h2', 'p']):
    if linha_texto.name == 'h2':
        contar_titulos += 1 # contar_titulos = contar_titulos + 1
    elif linha_texto.name == 'p':
        contar_paragrafos += 1 #aqui ele vai somar COntar_paragrafos

print('Total de titulos', contar_titulos) # aqui ele exibe
print('Total de paragrafos', contar_paragrafos)

# # exibir somente o texto das tag h2 e p
 for linha_texto in extracao.find_all(['h2, p']):
     if linha_texto.name == 'h2':
         titulo = linha_texto.texto.strip()
         print('Titulo: \n', titulo)
     elif linha_texto.name == 'p':
         paragrafo = linha_texto.text.strip()
         print('paragrafo: \n', paragrafo)

# Exibir tags aninhada
for titulo in extracao.find_all('h2'):
    print('\n titulo: ', titulo.text.strip())
    for link in titulo.find_next_siblings('p'):
        for a in link.find_all('a', href=True):
            print('text link: ', a.text.strip(), ' | url:', a["href"])