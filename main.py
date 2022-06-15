from controller.request import request
from controller.database import *


# criando banco e tabelas
create_database()

tableReading = Table('lendo')
tableReading.create_table()

tableIWTR = Table('ler')
tableIWTR.create_table()

tableRead = Table('lido')
tableRead.create_table()

show_database()




# 9788595081536 -> Teste ISBN
# 8524905549 -> Teste ISBN 
# 8573081082 -> Teste ISBN 
# pattern = re.compile(r"\[\'|\'\]") -> Padrão para retornar uma string de lista em lista novamente