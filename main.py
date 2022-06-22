from flask import Flask, render_template,request
import pickle

#chamando nosso app
app = Flask(__name__)

#criando pagina central com o formulários
@app.route("/")
@app.route("/index")
def start_page():
    return render_template("index.html")

#criando modelo preditivo
@app.route("/predicao", methods=["POST"])
def start_pred():
    #variaveis que fazemos o request pelo forms
    salario = request.form.get("salario")
    idade = request.form.get("idade")
    divida = request.form.get("divida")
    #carregando o modelo pickle
    modelo =pickle.load(open("model.pkl", "rb"))
    #fazendo a predição
    predicao = modelo.predict([[salario, idade,divida]])
    resultado =str(predicao)

    #salvando os arquivos em um arquivo txt
    with open("predicao.txt", "w+") as file:
        file.seek(0)
        file.write(str(predicao))

    #retornando o resultado final com legenda
    return f""" Resultado Final: {resultado} ||| Leitura do resultado: Opção 0 - Crédito recusado; Opção 1 - Fornecer Crédito |||
    """
#rodando o arquivo no modulo principal
if __name__== "__main__":
    #rodando o app
    app.run(host="0.0.0.0", port=3000)