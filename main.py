from controller.request import request
from controller.database import *


# criando banco e tabelas
criaBanco()

tabelaLendo = Tabela('lendo')
tabelaLendo.criarTabela()

tabelaLer = Tabela('ler')
tabelaLer.criarTabela()

tabelaLido = Tabela('lido')
tabelaLido.criarTabela()

mostraTabelasBanco()


# colocando os dados inseridos no banco
isbn = input('insira o isbn: ')
dadosRetornados = request(isbn)
status = input('insira o status: ').strip().lower()
inicioLeitura = input('insira a data de incio da leitura: ')
fimLeitura = input('Insira a data de término da leitura: ')
dadosRetornados['status'] = status 
dadosRetornados['inicio_leitura'] = inicioLeitura
dadosRetornados['fim_leitura'] = fimLeitura

print(dadosRetornados)
while True:
    if status == "lendo":
        tabelaLendo.adicionarDados(dadosRetornados)
        break
    elif status == "ler":
        tabelaLer.adicionarDados(dadosRetornados)
        break
    elif status == "lido":
        tabelaLido.adicionarDados(dadosRetornados)
        break
    else:
        print('status invalido!')
        status = input('insira o status: ').strip().lower()
        dadosRetornados['status'] = status 

# 9788595081536 -> Teste ISBN
# 8524905549 -> Teste ISBN 
# 8573081082 -> Teste ISBN 
# pattern = re.compile(r"\[\'|\'\]") -> Padrão para retornar uma string de lista em lista novamente