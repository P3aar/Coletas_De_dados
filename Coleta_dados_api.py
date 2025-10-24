import requests

def enviar_arquivo():
    # caminho do arquivo para upload
    caminho = 'C:/Users/Yuri/Desktop/ANALYTICS/teste.xlsx'

    # Enviar o arquivo
    requisicao = requests.post( 'https://gofile.io/home', files={'file': open(caminho, 'rb')})

    saida_requisicao = requisicao.json()
    print(saida_requisicao)
    url = saida_requisicao['data']['DownloadPage']
    print("Arquivo enviado. Link para acesso:", url)

enviar_arquivo()

