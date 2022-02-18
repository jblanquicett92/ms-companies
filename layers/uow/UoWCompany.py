from ports.AbstractUnitOfWork import AbstractUnitOfWork 
from layers.repository.repository_company import RepositoryCompany 
from boot import bootstrapping

class SQLAlchemyCompany(AbstractUnitOfWork):
    
    def __init__(self, session_factory=bootstrapping()):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.company = RepositoryCompany(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()