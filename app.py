from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
# O nome 'db' é o nome do serviço que daremos ao Redis no docker-compose!
redis_db = Redis(host=os.getenv('HOST'), port=os.getenv('PORTA'))

@app.route('/')
def hello():
    # Tenta obter a contagem; se não existir, define como 1
    # 'incr' é um comando do Redis que incrementa o valor de uma chave
    count = redis_db.incr('hits')
    return f'Olá! Esta página foi visitada {count} vezes.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
