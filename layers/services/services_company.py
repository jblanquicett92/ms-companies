from layers.domain import model
from layers.domain.model import Companies
from layers.uow import UoWCompany as unit_of_work

def add_companies(companies : Companies, uow: unit_of_work.SQLAlchemyCompany):
    with uow:
        companyList = uow.company.list()
        companies = model.add_companies(companies, companyList)
        uow.session.close()
        return model.add_companies(companies, companyList)

def add_company(
    id: int, name:str, email:str, phone:str, is_active:bool, dummy_card:bool,
    uow: unit_of_work.SQLAlchemyCompany
):
    with uow:
        uow.company.add(model.Company(id, name, email, phone, is_active, dummy_card))
        uow.commit()

def get_company(id:int,
    uow: unit_of_work.SQLAlchemyCompany
):
    with uow:
        company = uow.company.get(id)
        uow.session.close()
        return company
        
