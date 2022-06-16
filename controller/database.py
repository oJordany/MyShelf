from curses import meta
import sqlite3
from random import randint

def create_database():
    con = sqlite3.connect('database/estante.db')
    con.commit()
    con.close()
    

def show_database(nameDatabase='estante'):
    con = sqlite3.connect(f'database/{nameDatabase}.db')
    cur = con.cursor()
    cur.execute('SELECT name from sqlite_master where type= "table"')
    tablesDatabase = cur.fetchall()
    print(tablesDatabase)
    print('\n')
    if tablesDatabase == []:
        print('Banco vazio')
    else:
        print(f'TABELAS DE \033[1;32m{nameDatabase}\033[m:')
        for table in tablesDatabase:
            color = randint(31,39)
            print(f'\033[1;{color}m{table[0]}\033[m', end = '   ')
    print('\n')

def query_database(nameDatabase='estante'):
    con = sqlite3.connect(f'database/{nameDatabase}.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM Books')
    allDatas = cur.fetchall()
    return allDatas

class Table:

    def __init__(self):
        con = sqlite3.connect('database/estante.db')
        cur = con.cursor()
        try:
            cur.execute(f'''CREATE TABLE Books
                            (ID integer, Type text, Title text, Author text, Publisher text, Publication_date integer, Language text, Start_of_Reading text, End_of_Reading text, Status text)''')
        except:
            pass
        finally:
            con.commit()
            con.close()


    def add_data(self, dados):
        con = sqlite3.connect('database/estante.db')
        cur = con.cursor() 

        cur.execute(f'''INSERT INTO Books VALUES 
                        ({dados['identifier']}, "{dados['type']}", "{dados['title']}", "{dados['author']}", 
                        {'"' if dados['publisher'] != '' else ''}{dados['publisher'] if dados['publisher'] != '' else 'NULL'}{'"' if dados['publisher'] != '' else ''}, 
                        {int(dados['year'])}, "{dados['language']}", 
                        {'"' if dados['start_of_reading'] != 'NULL' else ''}{dados['start_of_reading']}{'"' if dados['start_of_reading'] != 'NULL' else ''}, {'"' if dados['end_of_reading'] != 'NULL' else ''}{dados['end_of_reading']}{'"' if dados['end_of_reading'] != 'NULL' else ''},
                        "{dados['status']}" 
                        )''')

        con.commit()
        con.close()
