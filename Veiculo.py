from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///veidculos.db'
db = SQLAlchemy(app)

class Veiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(254)) # ex = Chevrolet
    nomeDescricao = db.Column(db.String(254)) # ex = gol city
    anoModelo = db.Column(db.String(254)) # ex = 2013/2014
    cor = db.Column(db.String(254)) # ex = azul
    placa = db.Column(db.String(254)) # ex = FjK2520
    renavam = db.Column(db.Integer)
    categoria = db.Column(db.String(254)) # ex = Ultilitário, Passeio, carga

