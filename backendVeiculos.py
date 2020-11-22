from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from veiculo import Veiculo
import os
app = Flask(__name__)
caminho = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(caminho, 'veiculos.bd')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + arquivobd
app.config['SQLAlCHEMY_TRACK_MODIFICATIOS'] = False
db = SQLAlchemy(app)



@app.route("/")
def padrao():
    return " backend operante"
app.run()