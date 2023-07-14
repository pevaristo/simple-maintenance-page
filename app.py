import bottle
from bottle import route, run, error

app = bottle.default_app()

@route('/')
def info():
    return 'Estamos em manutenção.'

@error(404)
def error404(error):
    return 'Estamos em manutenção.'

if __name__ == "__main__":
    run(host='localhost', port=8080)
