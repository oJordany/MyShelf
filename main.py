from controller.request import request
from interface.screens.HomeWindow import HomeWindow
from controller.database import *


# criando banco e tabelas
create_database()

home_window = HomeWindow()
home_window.generate_home_window()




# 9788595081536 -> Teste ISBN
# 8524905549 -> Teste ISBN 
# 8573081082 -> Teste ISBN 
# pattern = re.compile(r"\[\'|\'\]") -> Padrão para retornar uma string de lista em lista novamente