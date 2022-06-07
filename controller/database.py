import sqlite3
from random import randint

def criaBanco():
    con = sqlite3.connect('database/estante.db')
    con.commit()
    con.close()
    

def mostraTabelasBanco(nomeBanco='estante'):
    con = sqlite3.connect(f'database/{nomeBanco}.db')
    cur = con.cursor()
    cur.execute('SELECT name from sqlite_master where type= "table"')
    tabelasDoBanco = cur.fetchall()
    print(tabelasDoBanco)
    print('\n')
    if tabelasDoBanco == []:
        print('Banco vazio')
    else:
        print(f'TABELAS DE \033[1;32m{nomeBanco}\033[m:')
        for tabela in tabelasDoBanco:
            cor = randint(31,39)
            print(f'\033[1;{cor}m{tabela[0]}\033[m', end = '   ')
    print('\n')


class Tabela:
    def __init__(self, status, id='id', tipo='tipo', titulo='titulo', autor='autor', anoPubli='ano_publicacao',
                editora='editora', inicioLeitura='inicio_leitura', fimLeitura='fim_leitura'):
        self.status = status 
        self.id = id
        self.tipo = tipo
        self.titulo = titulo 
        self.autor = autor
        self.anoPubli = anoPubli
        self.editora = editora 
        self.inicioLeitura = inicioLeitura
        self.fimLeitura = fimLeitura

    def criarTabela(self):
        con = sqlite3.connect('database/estante.db')
        cur = con.cursor()
        try:
            cur.execute(f'''CREATE TABLE {self.status} 
                            (id integer, tipo text, titulo text, autores text, ano_publicacao integer, editora text, idioma text, status text, inicio_leitura text, fim_leitura text)''')
        except:
            pass
        finally:
            con.commit()
            con.close()


    def adicionarDados(self, dados):
        con = sqlite3.connect('database/estante.db')
        cur = con.cursor() 

        cur.execute(f'''INSERT INTO {self.status} VALUES 
                        ({dados['identifier']}, "{dados['type']}", "{dados['title']}", "{dados['author']}", 
                        {dados['year']}, "{dados['publisher']}", "{dados['language']}", 
                        "{dados['status']}", "{dados['inicio_leitura']}", "{dados['fim_leitura']}" 
                        )''')

        con.commit()
        con.close()



    