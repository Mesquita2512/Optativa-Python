from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy 
import os 
app = Flask(__name__) 
caminho = os.path.dirname(os.path.abspath(__file__)) 
arquivobd = os.path.join(caminho, "veiculos.db") 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+arquivobd 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)