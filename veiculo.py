from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
app = Flask(__name__)
caminho = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(caminho, 'veiculos.bd')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + arquivobd
app.config['SQLAlCHEMY_TRACK_MODIFICATIOS'] = False
db = SQLAlchemy(app)

#eu trabalhei aki
class Veiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(254)) # ex = Chevrolet
    nomeDescricao = db.Column(db.String(254)) # ex = gol city
    anoModelo = db.Column(db.String(254)) # ex = 2013/2014
    cor = db.Column(db.String(254)) # ex = azul
    placa = db.Column(db.String(254)) # ex = FjK2520
    renavam = db.Column(db.Integer)
    categoria = db.Column(db.String(254)) # ex = Ultilitário, Passeio, carga
    def __str__(self) :
        return str(self.id) + ", " + self.marca + ", " + self.nomeDescricao + ", " + self.anoModelo + ", " +\
               self.cor + ", " + self.placa + ", " + str(self.renavam) + ", " + self.categoria
    def json(self):
        return{
            "id" : self.id,
            "marca" : self.marca,
            "nomeDescricao" : self.nomeDescricao,
            "anoModelo" : self.anoModelo,
            "cor" : self.cor,
            "placa" : self.placa,
            "renavam" : self.renavam,
            "categoria" : self.categoria
        }

if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)
    db.create_all()

    novo = Veiculo(marca = "vw", nomeDescricao = "golf gti", anoModelo="2015/2016", \
    cor = "cinza", placa = "aaa1111", renavam ="12345678965", categoria = "passeio")

    novo2 = Veiculo(marca = "hk", nomeDescricao = "Scania", anoModelo="2015/2016", \
    cor = "cinza", placa = "aaa1111", renavam ="12345678965", categoria = "Carga")


    db.session.add(novo)
    db.session.add(novo2)
    db.session.commit()
    todosVeiculos = db.session.query(Veiculo).all()


    for meusVeiculos in todosVeiculos:
        print(meusVeiculos)
    for vJson in todosVeiculos:
        print(vJson.json())
