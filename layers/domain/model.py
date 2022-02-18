import uuid
from typing import List

class User:

    def __init__(self, uuid: uuid, username: str, first_name: str,
        last_name: str, is_admin: bool, is_active: bool):
    
        self.uuid = uuid
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_admin = is_admin
        self.is_active = is_active
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.is_admin} {self.is_active}'


class CompanyClient(User):

    def __init__(self, uuid:uuid, username:str, first_name:str, last_name:str, is_admin:bool, 
    is_active:bool, is_banned: bool, is_deleted: bool, reservation: int , assign_credits: int):
        
        User.__init__(self, uuid,username,first_name, last_name, is_admin, is_active)
        self.is_banned = is_banned
        self.is_deleted = is_deleted
        self.reservation = reservation
        self.assign_credits = assign_credits

#bussiness rules: validar que sea un admin true
class AccountManager(User):

    def __init__(self, uuid:uuid, username:str, first_name:str, last_name:str, is_admin:bool, 
    is_active:bool):
       
        User.__init__(self, uuid,username,first_name, last_name, is_admin, is_active)


class Company:

    def __init__(self, id: int, name:str, email:str, phone:str, is_active:bool, dummy_card:bool):

        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.is_active = is_active
        self.dummy_card = dummy_card

        self._clients = dict()
        self._account_managers = dict()

    def client(self, uuid) -> CompanyClient:
        return self._clients[uuid]
    
    @property
    def clients(self) -> dict:
        return self._clients
    
    @property
    def active_clients(self) -> dict: 
        return [{client.uuid : client} for client in self._clients.values() if client.is_active==True]
    
    @property
    def clients_assigned_credit() -> dict:
        pass
    
    def account_manager(self, uuid) -> AccountManager:
        return self._account_managers[uuid]
    
    #bussiness rules: una compañia solo puede tener un account_manager
    @property
    def available_account_manager(self) -> int:
        ACCOUNT_MANAGER_PER_COMPANY=1
        return ACCOUNT_MANAGER_PER_COMPANY-len(self._account_managers)
    
    def add_client(self, client: CompanyClient):
        self._clients[client.uuid]=client
    
    def add_account_manager(self, account_manager: AccountManager):
        self._account_managers[account_manager.uuid]=account_manager
    
    def __str__(self):
        return f'{self.id} {self.name} {self.email} {self.phone} {self.is_active} ' + \
        f'{self.dummy_card}'

# esta clase realmente es un repository, preguntar a Paco
class Companies:

    def __init__(self):
        self._companies = dict()

    @property
    def list(self) -> dict:
        return self._companies
    
    def read(self, id:int) -> Company:
        return self._companies[id]
    
    def add(self, company:Company):
        self._companies[company.id]=company
    
    def delete(self, company:Company):
        del self._companies[company.id]
    
    @property    
    def number_of_companies(self) -> int:
        return len(self._companies)

def add_companies(companies: Companies, companyList: List[Company]):
    # [print(company) for company in companyList]
    [companies.add(company) for company in companyList]
    return companies
