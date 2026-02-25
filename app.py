from flask import Flask

# __name__ __main__
app = Flask(__name__)

#criacao de rota - receber e devolver informações (rota inicial "/"):
@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/about")
def about():
    return "página sobre"

#para executar agora (nao usar para clientes reais):
if __name__ == "__main__":
    app.run(debug=True)