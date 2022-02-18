from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey, Boolean
from sqlalchemy.orm import mapper

import layers.domain.model as model

metadata = MetaData()

company = Table(
    "companies_company",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255)),
    Column("email", String(255)),
    Column("phone", String(255)),
    Column("is_active", Boolean),
    Column("dummy_card", Boolean)
)


def start_mappers():
    mapper(model.Company, company) 
