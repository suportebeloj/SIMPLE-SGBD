from .orm import session
from .start_db import Categoria
from sqlalchemy.exc import IntegrityError, PendingRollbackError


class Inserir_categoria:
    def __init__(self, nome):
        self.nome = nome

    def inserir(self):
        try:
            categoria = Categoria(nome=self.nome)
            session.add(categoria)
            session.commit()
            return 'ok'
        except IntegrityError:
            session.rollback()
            return 'duplicado'

        finally:
            session.close()

    def session_flush(self):
        session.flush()
