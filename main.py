from flask import Flask, render_template
import pickle

app = Flask(__name__)
@app.route("/")
@app.route("/index")
def start_page():
    return render_template("index.html")

def start_pred():
    #falta criar modelo com o pickle: XGBoost
    pass


if __name__== "__main__":
    app.run(host="0.0.0.0", port=3000)