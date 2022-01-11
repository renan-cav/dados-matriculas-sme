from flask import Flask

app = Flask(__name__)
@app.route("/")
def inicio():
  return "<p>Dados Matrículas SME 2020</p>"
