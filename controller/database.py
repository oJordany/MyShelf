from io import BufferedReader
import sqlite3

def get_key(keyNumber):
    con = sqlite3.connect('database/estante.db')
    cur = con.cursor()
    cur.execute(f"SELECT key{keyNumber} FROM Keys")
    key = cur.fetchone()[0]
    con.close()
    return key

def create_database():
    con = sqlite3.connect('database/estante.db')
    con.commit()
    con.close()

def add_data_key(*key):
    con = sqlite3.connect('database/estante.db')
    with con:
        cur = con.cursor()
        cur.execute('''INSERT INTO Keys VALUES (?, ?)''', (memoryview(key[0]), memoryview(key[1])))

def update_data_key(key):
    con = sqlite3.connect('database/estante.db')
    with con:
        cur = con.cursor()
        cur.execute('''UPDATE Keys SET key2 = (?)''', (memoryview(key), ))
    
# def show_database(nameDatabase='estante'):
#     con = sqlite3.connect(f'database/{nameDatabase}.db')
#     cur = con.cursor()
#     cur.execute('SELECT name from sqlite_master where type= "table"')
#     tablesDatabase = cur.fetchall()
#     print(tablesDatabase)
#     print('\n')
#     if tablesDatabase == []:
#         print('Banco vazio')
#     else:
#         print(f'TABELAS DE \033[1;32m{nameDatabase}\033[m:')
#         for table in tablesDatabase:
#             color = randint(31,39)
#             print(f'\033[1;{color}m{table[0]}\033[m', end = '   ')
#     print('\n')

def query_database(nameDatabase='estante'):
    con = sqlite3.connect(f'database/{nameDatabase}.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM Books')
    allDatas = cur.fetchall()
    con.close()
    return allDatas

def remove_database(isbn, nameDatabase='estante'):
    con = sqlite3.connect(f'database/{nameDatabase}.db')
    cur = con.cursor()
    
    cur.execute(f'DELETE FROM Books WHERE ID = {isbn}')

    con.commit()
    con.close()

def search_database(search, nameDatabase='estante'):
    con = sqlite3.connect(f'database/{nameDatabase}.db')
    cur = con.cursor()

    try:
        cur.execute(f'SELECT * FROM Books WHERE ID = {search}')
        searchDatas = cur.fetchall()
    except:
        cur.execute(f'SELECT * FROM Books WHERE Type = "{search}"')
        searchDatas = cur.fetchall()
    if searchDatas == []:
        cur.execute(f'SELECT * FROM Books WHERE Title = "{search}"')
        searchDatas = cur.fetchall()
    if searchDatas == []:
        cur.execute(f'SELECT * FROM Books WHERE Author = "{search}"')
        searchDatas = cur.fetchall()
    if searchDatas == []:
        cur.execute(f'SELECT * FROM Books WHERE Publisher = "{search}"')
        searchDatas = cur.fetchall()
    if searchDatas == []:
        try:
            cur.execute(f'SELECT * FROM Books WHERE Publicate_date = {search}')
            searchDatas = cur.fetchall()
        except:
            pass
    if searchDatas == []:
        cur.execute(f'SELECT * FROM Books WHERE Language = "{search}"')
        searchDatas = cur.fetchall()
    if searchDatas == []:
        cur.execute(f'SELECT * FROM Books WHERE Start_of_Reading = "{search}"')
        searchDatas = cur.fetchall()
    if searchDatas == []:
        cur.execute(f'SELECT * FROM Books WHERE End_of_Reading = "{search}"')
        searchDatas = cur.fetchall()
    if searchDatas == []:
        cur.execute(f'SELECT * FROM Books WHERE Status = "{search}"')
        searchDatas = cur.fetchall()
    con.close()
    return searchDatas

def check_existence(isbn, nameDatabase='estante'):
    con = sqlite3.connect(f'database/{nameDatabase}.db')
    cur = con.cursor()
    try: 
        cur.execute(f'SELECT * FROM Books WHERE ID = {isbn}')
        book = cur.fetchall()
        if book != []:
            return True
        else:
            return False
    except:
        return False
    finally:
        con.close()

def change_status(isbn, nameDatabase='estante'):
    from datetime import date
    endDate = str(date.today())
    con = sqlite3.connect(f'database/{nameDatabase}.db')
    cur = con.cursor()

    cur.execute(f'''UPDATE Books 
        SET End_of_Reading = "{endDate}",
            Status = "read"
        WHERE ID = {isbn}''')

    con.commit()
    con.close()
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
                        ({dados['identifier']}, 
                        "{dados['type']}", 
                        "{dados['title']}", 
                        {'"' if dados['author'] != 'NULL' else ''}{dados['author']}{'"' if dados['author'] != 'NULL' else ''}, 
                        {'"' if dados['publisher'] != '' else ''}{dados['publisher'] if dados['publisher'] != '' else 'NULL'}{'"' if dados['publisher'] != '' else ''}, 
                        {int(dados['year']) if dados['year'].isdigit() else 'NULL'}, 
                        {'"' if dados['language'] != 'NULL' else ''}{dados['language']}{'"' if dados['language'] != 'NULL' else ''},  
                        {'"' if dados['start_of_reading'] != 'NULL' else ''}{dados['start_of_reading']}{'"' if dados['start_of_reading'] != 'NULL' else ''}, 
                        {'"' if dados['end_of_reading'] != 'NULL' else ''}{dados['end_of_reading']}{'"' if dados['end_of_reading'] != 'NULL' else ''},
                        "{dados['status']}" 
                        )''')

        con.commit()
        con.close()
