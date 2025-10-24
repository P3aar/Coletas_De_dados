import pymysql
import pandas as pd
from sqlalchemy import create_engine


def conexao_mysql(host, user, password, db, table):
    # Criar conexao
    conn = pymysql.connect(host=host, user=user, password=password, db=db)

    cursor = conn.cursor()

    # Executar consultar
    query = 'select * from ' + table + ' limit 10'
    cursor.execute(query)

    # Buscar resultados
    resultados = cursor.fetchall()

    # Exibir os resultados
    print('Tabela MySQL:')
    for linha in resultados:
        print(linha)

    # Fechar a conexao
    cursor.close()
    conn.close()

def df_conexao_mysql(host, user, password, db, table):
    # Criar conexao
    conn = create_engine('mysql+pymysql://' + user + ':' + password + '@' + host + '/' + db)

    # Executar consultar e salvar em um dataframe
    query = 'select * from ' + table
    df = pd.read_sql(query, conn)

    # exibir os resultados
    print('tabela mysql com dataframe: \n', df.head())

    # fechar a conexao
    conn.dispose()
    return df



def conexao_excel(path):
    # ler arquivo excel
    df = pd.read_excel(path)
    print('dados excel: \n', df.head())

    # escrever arquivo csv
    df.to_csv('dados.csv', index=False)


def conexao_csv(path):
    # ler arquivo csv
    df = pd.read_csv(path)
    print('dados csv: \n', df.head())

    # escrever arquivos json
    df.to_json('dados.json', orient='records', index=False)

conexao_mysql('localhost', 'root', 'Yuriborges06', 'loja_informatica', 'cliente')

df_cliente = df_conexao_mysql('localhost', 'root', 'Yuriborges06', 'loja_informatica', 'cliente')
df_cliente.to_excel('dados.xlsx', index=False)

conexao_excel('dados.xlsx')

conexao_csv('dados.csv')
