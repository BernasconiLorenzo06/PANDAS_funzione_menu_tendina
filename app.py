from flask import Flask, render_template, request
app = Flask(__name__)
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/consegne-vaccini-latest.csv")

@app.route('/')
def home():
    listaregione = list(set(df["reg"]))
    return render_template('home.html',lista = listaregione)



@app.route('/esercizio1',methods = ["GET"])
def esercizio1():
    regioneInput = request.args.get('regioneInput')
    table = df[df["reg"] == regioneInput].groupby("reg")[["numero_dosi"]].sum().reset_index()
    tabella = table.to_html()
    return render_template('esercizio1.html', tabella = tabella)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)