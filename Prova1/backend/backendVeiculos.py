import config
import modelo


@config.app.route("/")
def padrao():
    return "bem vindo ao backend"

@config.app.route("/listar_veiculos")
def listar_veiculos():
    veiculos = config.db.session.query(modelo.Veiculo).all()
    retorno = []    
    for p in veiculos:
        retorno.append(p.json())
    resposta = config.jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

@config.app.route("/incluir_planta", methods=['post'])
def incluir_veiculo():
    dados = config.request.get_json()
    novoVeiculo = modelo.Veiculo(**dados)
    config.db.session.add(novoVeiculo)
    config.db.session.commit()
    return {"resultado":'ok'}

config.app.run(debug=True)
