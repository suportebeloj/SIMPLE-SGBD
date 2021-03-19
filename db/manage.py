from .conn import conexao
from pymysql.err import IntegrityError


class Manager:
    @classmethod
    def start(cls):
        tabelas = ['saida', 'entrada', 'categorias', 'relatorio']
        for tabela in tabelas:
            if tabela == 'categorias':
                sql = 'create table if not EXISTS categorias(' \
                      '`id` int AUTO_INCREMENT,' \
                      '`nome` varchar(150) not NULL UNIQUE,' \
                      '`criado_em` datetime NOT NULL,' \
                      'PRIMARY KEY(`id`)' \
                      ');'
                print('Criando tabela categorias ... ', end='')

                with conexao() as conn:
                    with conn.cursor() as cursor:
                        cursor.execute(sql)

                print('\033[1;32mOK\033[m')

            elif tabela == 'relatorio':
                pass
            else:
                sql = f'CREATE TABLE if not EXISTS {tabela} (' \
                      '`id` int AUTO_INCREMENT,' \
                      '`descricao` varchar(255) not NULL,' \
                      '`sobre` varchar(1000),' \
                      '`criado_em` datetime NOT NULL,' \
                      '`data` date not NULL,' \
                      'PRIMARY KEY(id)' \
                      ');'
                print(f'Criando tabela {tabela} ... ', end='')
                with conexao() as conn:
                    with conn.cursor() as cursor:
                        cursor.execute(sql)

                print('\033[1;32mOK\033[m')

    @classmethod
    def inserir(cls, tabela=None, **kwargs):
        """
        Manager.inserir(table=Name_table, campos=kwargs)
        """
        if not tabela:
            print('Nome da tabela não foi informado.')
            return
        table = tabela
        values_str = str('%s, ' * len(kwargs.keys()))[:-2]
        keys_str = ''

        for k, v in enumerate(kwargs.keys()):
            keys_str += f'`{v}`, '

        sql = f'INSERT INTO `{table}` ({keys_str[:-2]}) VALUES({values_str});'

        with conexao() as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(sql, tuple(kwargs.values()))
                except IntegrityError as err:
                    if err.args[0] == 1062:
                        print(f'Valor duplicado no banco de dados "{table}":\n'
                              f'{kwargs["nome"]}')

            conn.commit()

    @classmethod
    def listar_tudo(cls, tabela=None):

        sql = f'SELECT * FROM {tabela};'

        with conexao() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()

    @classmethod
    def atualizar(cls, table=None, id=None, **kwargs):
        campos = ''
        for k, v in kwargs.items():
            campos += f'{k}="{v}", '

        sql = f'UPDATE {table} SET {campos[:-2]} WHERE id={id}'

        with conexao() as conn:
            with conn.cursor() as cursor:
                if cls._get(table, id=id):
                    cursor.execute(sql)
                    conn.commit()
                else:
                    print(f'Objeto não existe no banco de dados {table}')

    @classmethod
    def deletar(cls, table, id):
        sql = f'DELETE FROM {table} WHERE id={id}'
        with conexao() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                conn.commit()

    @classmethod
    def _get(cls, table, **kwargs):
        field = ''
        for k, v in kwargs.items(): field += f'{k}={v}'

        sql = f'SELECT * FROM {table} WHERE {field}'
        with conexao() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()

                if result:
                    return True
                return False

    @classmethod
    def _table_existe(cls, table_name=None):
        sql = 'show tables;'

        with conexao() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                result = [r['Tables_in_testes'] for r in cursor.fetchall()]

                if table_name in result:
                    return True
                return False
