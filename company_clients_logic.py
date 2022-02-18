import layers.domain.model as model

companyClient1=model.CompanyClient("0d14fbaa-8cd6-11e7-b2ed-28d244cd6e76", "jblanquicett", "Jorge", "Blanquicett", False, True, False,  False, 0, 0)
companyClient2=model.CompanyClient("0d14fbaa-8cd6-11e7-b2ed-28d555cd6e76", "cmartinez", "Cecilia", "Martinez", False, False, False,  False, 0, 0)

print(companyClient1.is_admin)
print(companyClient2.is_admin)

company1=model.Company(1,'Apple', 'apple@mail.com','6625330', True, True)

#add_client
company1.add_client(companyClient1)
company1.add_client(companyClient2)

#list_clients
[print(client) for client in company1.clients.values()]

#read_client
print(company1.client("0d14fbaa-8cd6-11e7-b2ed-28d555cd6e76"))

#add_credits_to_a_client
print(company1.client("0d14fbaa-8cd6-11e7-b2ed-28d555cd6e76").assign_credits)
company1.client("0d14fbaa-8cd6-11e7-b2ed-28d555cd6e76").assign_credits=500
print(company1.client("0d14fbaa-8cd6-11e7-b2ed-28d555cd6e76").assign_credits)

#list_active_clients
print(type(company1.active_clients))
[print(client) for client in company1.active_clients]