from flask import Blueprint
from layers.controller import controller_company

company = Blueprint("company", __name__, url_prefix="/v3/company")
companies = Blueprint("companies", __name__, url_prefix="/v3/companies")

@company.post('/')
def create():
    return {"status": 201, "resource":"created company"}, 201

@company.get('/<int:id>')
def read(id):
    return controller_company.read_json_format(id)

@companies.get('/')
def list():
    return controller_company.list_json_format()