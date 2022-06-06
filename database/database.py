import sqlite3
from random import randint

def criaBanco():
    con = sqlite3.connect('estante.db')
    con.commit()
    con.close()
    
class Tabela:
    def __init__(self, status, id='id', tipo='tipo', titulo='titulo', autor='autor(es', anoPubli='ano_publicacao',
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
        con = sqlite3.connect('estante.db')
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
        con = sqlite3.connect('estante.db')
        cur = con.cursor() 

        cur.execute(f'''INSERT INTO {self.status} VALUES 
                        ({dados['identifier']}, "{dados['type']})", "{dados['title']}", "{dados['author']}", 
                        {dados['year']}, "{dados['publisher']}", "{dados['language']}", 
                        "{dados['status']}", "{dados['inicio_leitura']}", "{dados['fim_leitura']}" 
                        )''')

        con.commit()
        con.close()


    def mostraTabelasBanco(self, nomeBanco='estante'):
        con = sqlite3.connect(f'{nomeBanco}.db')
        cur = con.cursor()
        cur.execute('SELECT name from sqlite_master where type= "table"')
        tabelasDoBanco = cur.fetchall()
        print('\n')
        if tabelasDoBanco == []:
            print('Banco vazio')
        else:
            print(f'TABELAS DE \033[1;32m{nomeBanco}\033[m:')
            for tabela in tabelasDoBanco:
                cor = randint(31,39)
            print(f'\033[1;{cor}m{tabela[0]}\033[m', end = '   ')
        print('\n')

    def printaBancoEmFormatoTabela(self, nomeTabela, order='', baseDeDados='estante'):
        # Tratando o order
        if order != '':
            order = f'ORDER BY {order}'
        else:
            order = ''
        # Usando o sqlite 3
        con = sqlite3.connect(f'{baseDeDados}.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute(f'SELECT * FROM {nomeTabela}')
        r = cur.fetchone()
        # Encontrando o maior membro da tabela
        biggestMember= 0
        
        for key in r.keys():
            if len(str(key)) > biggestMember:
                biggestMember = len(str(key))

        
        for row in cur.execute(f'SELECT * FROM {nomeTabela}'):
            for data in row:
                if len(str(data)) > biggestMember:
                    biggestMember = len(str(data))
                
        biggestMember += 3

        # Table Header
        for i, key in enumerate(r.keys()):
            if i != len(r.keys()) - 1:
                print(f'{key}{" "*(biggestMember-len(key))}|', end='')
            else:
                print(f'{key}{" "*(biggestMember-len(key))}', end='')
        
        print()
        print('-'*((biggestMember)*len(r.keys())+len(r.keys())-1))

        # Table Body
        for row in cur.execute(f'SELECT * FROM {nomeTabela} {order}'):
            if row[0] > 0:
                for i in range(0, len(row)):
                    if i != len(row) - 1:
                        print(f'{row[i]}{" "*(biggestMember-len(str(row[i])))}|', end='')
                    else:
                        print(f'{row[i]}{" "*(biggestMember-len(str(row[i])))}')
        
        print()
        con.close()


        
