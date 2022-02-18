import layers.domain.model as model
from src.conftest import in_memory_db, session


def test_company_mapper_can_save(session):
    
    new_company = model.Company(161, 'company2', 'company2@com.com', '0', False, False)
    session.add(new_company)
    session.commit()
    last_company_row = list(session.execute('SELECT name, email, phone FROM companies_company ORDER BY id DESC LIMIT 1'))
    session.close()
    assert last_company_row == [("company2", "company2@com.com", '0')]
