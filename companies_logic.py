import layers.domain.model as model

# account_manager=model.AccountManager("0d14fbaa-8cd6-11e7-b2ed-28d244cd6e76", "jblanquicett", "Jorge", "Blanquicett", False, True)

#create
company1=model.Company(1,'Apple', 'apple@mail.com','6625330', True, True)
company2=model.Company(2,'Windows', 'wind@mail.com','666', True, True)
company4=model.Company(4,'Tesla', 'tes@mail.com','111', True, True)
company5=model.Company(5,'Amazon', 'amz@mail.com','222', True, True)
company6=model.Company(6,'Netflix', 'net@mail.com','333', True, True)

companyDict = {}
companyDict[company1.id] = company1
companyDict[company2.id] = company2
companyDict[company4.id] = company4
companyDict[company5.id] = company5

# Add companies & List
companies= model.Companies()
[companies.add(company) for company in companyDict.values()]

# Update
print(companies.read(4))
company4 = companies.read(4)
company4.name='Facebook'
print(companies.read(4))

