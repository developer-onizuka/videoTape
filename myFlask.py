#from flask import Flask
import flask

#app = Flask(__name__)
app = flask.Flask(__name__)

@app.route('/')
def index():
    #return '__name__ == ' + __name__
    return 'Hello World!'

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)


def newFunc():
    return 'DEADBEAF'

xyz = newFunc()
