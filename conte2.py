from contentful_management import Client

client = Client('CFPAT-hGVwkxMa8foEyTrV9IUnz3GU2srKlDk5kDQec4BkFfQ')

environment = client.environments('eb1ljr3ipitt').all()
print(environment)