from myFlask import app

def getRequest():
    app.config['TESTING'] = True
    client = app.test_client()
    response = client.get('/')
    print(response.data)

getRequest()
