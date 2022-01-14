import base64
import json
import os

import gspread
from flask import Flask, render_template
import pandas as pd

spreadsheet_id = os.environ["GOOGLE_SHEET_ID"]
cont_codificado = os.environ["GOOGLE_SHEET_CREDENTIAL"]
conteudo = base64.b64decode(cont_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials)
spreadsheet = service_account.open_by_key(spreadsheet_id)
worksheet = spreadsheet.worksheet("df_turmas_2020")

dados = pd.DataFrame(worksheet.get_all_records())
dados_html = dados.to_html()

app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template("home.html")

@app.route("/sobre")
def sobre():
  return render_template("sobre.html")
