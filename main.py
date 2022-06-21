from flask import Flask, render_template,request
import pickle

app = Flask(__name__)
@app.route("/")
@app.route("/index")
def start_page():
    return render_template("index.html")

@app.route("/start_pred", methods=["POST"])
def start_pred():
    salario = request.form.get("salario")
    idade = request.form.get("idade")
    divida = request.form.get("divida")
    modelo =pickle.load(open("model.pkl", "rb"))
    predicao = modelo.predict([[salario, idade,divida]])
    return str(predicao)


if __name__== "__main__":
    app.run(host="0.0.0.0", port=3000)