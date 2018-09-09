import bottle
from bottle import route, run

app = bottle.default_app()

@route('/')
def info():
    return 'We\'ll be back shortly. Thank you for your visit.'

if __name__ == "__main__":
    run(host='localhost', port=8080)
