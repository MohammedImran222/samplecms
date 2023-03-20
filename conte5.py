'''from contentful_management import Client

client = Client('CFPAT-hGVwkxMa8foEyTrV9IUnz3GU2srKlDk5kDQec4BkFfQ')

spaces = client.('eb1ljr3ipitt')
print(spaces)'''
from contentful import Client

client = Client('eb1ljr3ipitt',
                '1LRArm7-5ppsvEyut7meLoUGtaaURnfkJ8osSVjtm30',
                environment='master' )

entry = client._proxy_parameters()
print(entry)