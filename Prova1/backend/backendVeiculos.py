from logging import exception
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

@config.app.route("/incluir_veiculo", methods=['post'])
def incluir_veiculo():
    
    dados = config.request.get_json()
    print(dados)
    try: # tentar execultar a inserção
        novoVeiculo = modelo.Veiculo(dados) # criar um veiculo com o construtor
        config.db.session.add(novoVeiculo) # adiciona o veiculo no banco de dados
        config.db.session.commit() # efetiva a operação realizada
        resposta = config.jsonify({"resultado": "ok", "detalhes": "ok"})
    except exception as e: # se houver erro este código é execultado
        resposta = config.jsonify({"resultado": "erro", "detalhes": str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return {"resultado":'ok'} # responder!

config.app.run(debug=True)
