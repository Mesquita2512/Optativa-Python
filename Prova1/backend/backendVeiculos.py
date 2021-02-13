from logging import exception
import config
import modelo

@config.app.route("/")
def padrao():
    return "bem vindo ao backend"

#LISTANDO OS Veiculos
@config.app.route("/listar_veiculos")
def listar_veiculos():
    veiculos = config.db.session.query(modelo.Veiculo).all()
    retorno = []    
    for p in veiculos:
        retorno.append(p.json())
    resposta = config.jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

#ADICIONANDO UM ITEM
@config.app.route("/incluir_veiculo", methods=['post'])
def incluir_veiculo():
    resposta = config.jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = config.request.get_json()
    try: # tentar execultar a inserção
        novoVeiculo = modelo.Veiculo(**dados) # criar um veiculo com o construtor
        config.db.session.add(novoVeiculo) # adiciona o veiculo no banco de dados
        config.db.session.commit() # efetiva a operação realizada
    except exception as E: # se houver erro este código é execultado
        resposta = config.jsonify({"resultado": "erro", "detalhes": str(E)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!

#DELETANDO UM ITEM
@config.app.route("/excluir_veiculo/<int:veiculo_id>", methods=['DELETE'])
def excluir_veiculo(veiculo_id):
    resposta = config.jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        modelo.Veiculo.query.filter(modelo.Veiculo.id == veiculo_id).delete()
        config.db.session.commit()
    except Exception as e:
        resposta = config.jsonify({"resultado": "erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

config.app.run(debug=True)
