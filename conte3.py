from contentful import Client

client = Client('eb1ljr3ipitt',
                '1LRArm7-5ppsvEyut7meLoUGtaaURnfkJ8osSVjtm30',
                environment='master' )

entry = client.entries()
print(entry)