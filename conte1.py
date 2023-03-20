from contentful_management import Client

client = Client('CFPAT-hGVwkxMa8foEyTrV9IUnz3GU2srKlDk5kDQec4BkFfQ')

spaces = client.spaces().all()
print(spaces)