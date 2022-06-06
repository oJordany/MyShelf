from api.request import request
from database.database import *


# criando banco e tabelas
criaBanco()
tabela = Tabela('lendo')
tabela.criarTabela()
tabela.mostraTabelasBanco()


# colocando os dados inseridos no banco
isbn = input('insira o isbn: ')
dadosRetornados = request(isbn)
status = input('insira o status: ')
inicioLeitura = input('insira a data de incio da leitura: ')
fimLeitura = input('Insira a data de término da leitura: ')
dadosRetornados['status'] = status 
dadosRetornados['inicio_leitura'] = inicioLeitura
dadosRetornados['fim_leitura'] = fimLeitura

print(dadosRetornados)

tabela.adicionarDados(dadosRetornados)

tabela.printaBancoEmFormatoTabela(tabela.status, tabela.id)

# 9788595081536 -> Teste ISBN
# 9788595081536 -> Teste ISBN 
# pattern = re.compile(r"\[\'|\'\]") -> Padrão para retornar uma string de lista em lista novamente