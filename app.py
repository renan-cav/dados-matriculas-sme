import base64
import json
import os

import gspread
from flask import Flask
import pandas as pd

spreadsheet_id = os.environ["GOOGLE_SHEET_ID"]
cont_codificado = os.environ["GOOGLE_SHEET_CREDENTIAL"]
conteudo = base64.b64decode(cont_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials)
spreadsheet = service_account.open_by_key(spreadsheet_id)
worksheet = spreadsheet.worksheet("df_turmas_2020")

dados = pd.DataFrame(worksheet.get_all_records())

app = Flask(__name__)

@app.route("/")
def inicio():
  return "<p> Página inicial</p>"

@app.route("/sobre")
def sobre():
  return "<p> Desenvolvido por Renan Cavalcante Eugenio como projeto para o curso de pós-graduação de jornalismo de dados, automação e data storytelling do Instituto Insper</p>"

@app.route("/dados")
def inicio():
  return dados.to_html()
