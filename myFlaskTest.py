from myFlask import app
from myFlask import xyz

def getRequest():
    app.testing = True
    client = app.test_client()
    response = client.get('/')
    print(response.data)

getRequest()

print(xyz)
