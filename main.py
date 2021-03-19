from db.manage import Manager
from ctrl.list_registers import DataControl
from datetime import datetime

if __name__ == '__main__':
    # Manager.start()
    hoje = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Manager.inserir(tabela='categorias', nome='Laser', criado_em=f"{hoje}")
    # Manager.atualizar('categorias', 1, nome='Roupas', )

    DataControl.show('categorias')
