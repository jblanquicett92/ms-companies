import layers.domain.model as model
from ports.AbstractRepository import AbstractRepository 

class RepositoryCompany(AbstractRepository):
    
    def __init__(self, session):
        self.session = session

    def add(self, company):
        self.session.add(company)

    def get(self, id):
        return self.session.query(model.Company).filter_by(id=id).one()

    #detalle: Hijo y Padre deben tener comportamiento
    def list(self):
        return self.session.query(model.Company).all()