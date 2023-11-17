from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Aula de IAC Infrastructure as Code com Gabriela de Lima"