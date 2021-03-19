from db.manage import Manager


class DataControl:
    @classmethod
    def show(cls, table=None):
        if not table:
            print('Informe o nome da tabela.')
            return

        if Manager._table_existe(table):
            result = Manager.listar_tudo(table)
            if len(result) > 0:
                for i in Manager.listar_tudo(table): print(i)
            else:
                print(f'Sem registros na tabela "{table}".')
        else:
            print(f'Tabela "{table}" não foi encontrada.')
