from layers.domain import model
from layers.uow import UoWCompany as uow
from layers.services.services_company import get_company, add_companies
from layers.presenter import serializer
from src.utils.http_responses import Response

def read_json_format(id:int):

    company_schema = serializer.CompanySchema()
    company_serializer = company_schema.dump(get_company(id, uow.SQLAlchemyCompany()))
    return Response(company_serializer, 200).build_response("company")


def list_json_format():
    companies= model.Companies()
    companies=add_companies(companies, uow.SQLAlchemyCompany())
    company_schema = serializer.CompanySchema()
    companies_serializer = [company_schema.dump(company) for company in companies.list.values()]
    return Response(companies_serializer, 200).build_list_response("companies")