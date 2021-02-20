import config



#Empresa
class Empresa(config.db.Model):
    id = config.db.Column(config.db.Integer, primary_key=True)
    nome = config.db.Column(config.db.String(254))
    cnpj = config.db.Column(config.db.String(254))
    endereco = config.db.Column(config.db.String(254))
    telefone = config.db.Column(config.db.String(254))
    

    def __str__(self) -> str:
        return str(self.id) + ", " + self.nome + ", " + self.cnpj + ", " + self.endereco + ", " +\
               self.telefone

    def json(self):
        return{
            "id" : self.id,
            "nome" : self.nome,
            "cnpj" : self.cnpj,
            "endereco" : self.endereco,
            "telefone" : self.telefone
        }

#Veículo
class Veiculo(config.db.Model):
    id = config.db.Column(config.db.Integer, primary_key=True)
    marca = config.db.Column(config.db.String(254)) # ex = Chevrolet
    nomeDescricao = config.db.Column(config.db.String(254)) # ex = gol city
    anoModelo = config.db.Column(config.db.String(254)) # ex = 2013/2014
    cor = config.db.Column(config.db.String(254)) # ex = azul
    placa = config.db.Column(config.db.String(254)) # ex = FjK2520
    renavam = config.db.Column(config.db.Integer)
    categoria = config.db.Column(config.db.String(254)) # ex = Ultilitário, Passeio, carga
    #chave estrangeira
    idEmpresa = config.db.Column(config.db.Integer, config.db.ForeignKey(Empresa.id), nullable=False)
    # atributo de relacionamento, para acesso aos dados via objeto
    empresa = config.db.relationship("Empresa")

    def __str__(self) -> str:
        return str(self.id) + ", " + self.marca + ", " + self.nomeDescricao + ", " + self.anoModelo + ", " +\
               self.cor + ", " + self.placa + ", " + str(self.renavam) + ", " + self.categoria + ", " + str(self.empresa)
               # o str aciona o __str__ da classe Empresa

    def json(self):
        return{
            "id" : self.id,
            "marca" : self.marca,
            "nomeDescricao" : self.nomeDescricao,
            "anoModelo" : self.anoModelo,
            "cor" : self.cor,
            "placa" : self.placa,
            "renavam" : self.renavam,
            "categoria" : self.categoria,
            "idEmpresa":self.idEmpresa,
            "empresa":self.empresa.json() 
        }


#Habilitação
class Habilitacao(config.db.Model):
    id = config.db.Column(config.db.Integer, primary_key=True)
    numero = config.db.Column(config.db.Integer)
    categoria = config.db.Column(config.db.String(254))
    dataValidade = config.db.Column(config.db.String(254))

    def __str__(self) -> str:
        return str(self.id) + ", " + str(self.numero) + ", " + self.categoria + ", " + self.dataValidade

    def json(self):
        return{
            "id" : self.id,
            "numero" : self.numero,
            "categoria" : self.categoria,
            "dataValidade" : self.dataValidade
        }

#Motorista
class Motorista(config.db.Model):
    id = config.db.Column(config.db.Integer, primary_key=True)
    nome = config.db.Column(config.db.String(254))
    cpf = config.db.Column(config.db.Integer)
    dataNascimento = config.db.Column(config.db.String(254))
    idade = config.db.Column(config.db.Integer)
    endereco = config.db.Column(config.db.String(254))
    #chave estrangeira
    idHabilitacao = config.db.Column(config.db.Integer, config.db.ForeignKey(Habilitacao.id), nullable=False)
    # atributo de relacionamento, para acesso aos dados via objeto
    habilitacao = config.db.relationship("Habilitacao")

    def __str__(self) -> str:
        return str(self.id) + ", " + self.nome + ", " + str(self.cpf) + ", " + self.dataNascimento + ", " +\
               str(self.idade) + ", " + self.endereco + ", " + str(self.habilitacao)
               # o str aciona o __str__ da Habilitação

    def json(self):
        return{
            "id" : self.id,
            "nome" : self.nome,
            "cpf" : self.cpf,
            "dataNascimento" : self.dataNascimento,
            "idade" : self.idade,
            "endereco" : self.endereco,
            "idHabilitacao":self.idHabilitacao,
            "habilitacao":self.habilitacao.json() 
        }

#TipoCombustivel
class TipoCombustivel(config.db.Model):
    id = config.db.Column(config.db.Integer, primary_key=True)
    tipo = config.db.Column(config.db.String(254))
    valor = config.db.Column(config.db.Integer)

    def __str__(self) -> str:
        return str(self.id) + ", " + self.tipo + ", " + str(self.valor)

    def json(self):
        return{
            "id" : self.id,
            "tipo" : self.tipo,
            "valor" : self.valor
        }

#Abastecimento
class Abastecimento(config.db.Model):
    id = config.db.Column(config.db.Integer, primary_key=True)
    posto = config.db.Column(config.db.String(254))
    quantidade = config.db.Column(config.db.Integer)
    quilometragem = config.db.Column(config.db.Integer)
    data = config.db.Column(config.db.String(254))
    valorTotal = config.db.Column(config.db.Integer)
    #chave estrangeira
    idMotorista = config.db.Column(config.db.Integer, config.db.ForeignKey(Motorista.id), nullable=False)
    idVeiculo = config.db.Column(config.db.Integer, config.db.ForeignKey(Veiculo.id), nullable=False)
    idTipoCobustivel = config.db.Column(config.db.Integer, config.db.ForeignKey(TipoCombustivel.id), nullable=False)    
    # atributo de relacionamento, para acesso aos dados via objeto
    motorista = config.db.relationship("Motorista")
    veiculo = config.db.relationship("Veiculo")
    tipoCombustive = config.db.relationship("TipoCombustivel")

    def __str__(self) -> str:
        return str(self.id) + ", " + self.posto + ", " + str(self.quantidade) + ", " + str(self.quilometragem) + ", " +\
               self.data + ", " + str(self.valorTotal) + ", " + str(self.motorista + ", " + str(self.veiculo) + ", " +\
                str(self.tipoCombustive))
               # o str aciona o __str__ da Habilitação

    def json(self):
        return{
            "id" : self.id,
            "posto" : self.posto,
            "quantidade" : self.quantidade,
            "quilometragem" : self.quilometragem,
            "data" : self.data,
            "valorTotal" : self.valorTotal,
            "idMotorista":self.idMotorista,
            "motorista":self.motorista.json(),
            "idVeiculo":self.idVeiculo,
            "veiculo":self.veiculo.json(),
            "idTipoCombustivel":self.idTipoCobustivel,
            "tipoCombustivel":self.tipoCombustive.json()  
        }

    def calcularValorTotal():
        valorTotal = 0
        if TipoCombustivel.tipo == "gasolina":
            valorTotal = TipoCombustivel.valor * Abastecimento.quantidade
        elif TipoCombustivel == "diesel":
            valorTotal = TipoCombustivel.valor * Abastecimento.quantidade
        return valorTotal


if __name__ == "__main__":

    if config.os.path.exists(config.arquivobd):
        config.os.remove(config.arquivobd)
    config.db.create_all()

    #Teste Empresa
    novaE1 = Empresa(nome = "transportes suleicarias", cnpj = "555555555", endereco="rua das maricas", \
    telefone = "583696369")
    novaE2 = Empresa(nome = "meredes transportadora", cnpj = "222222222", endereco="rua das flores", \
    telefone = "4785858585")
    config.db.session.add(novaE1)
    config.db.session.add(novaE2)
    config.db.session.commit()
    print("Teste Empresa")
    print(novaE1)
    print(novaE2.json())
    print("--------------------------------------------------------------------------")

    #Teste Veículo
    novoV1 = Veiculo(marca = "hk", nomeDescricao = "Scania", anoModelo="2015/2016", \
    cor = "cinza", placa = "aaa1111", renavam ="12345678965", categoria = "Carga", empresa = novaE1)
    novoV2 = Veiculo(marca = "Scania", nomeDescricao = "Scania", anoModelo="2016/2016", \
    cor = "preto", placa = "aaa1123", renavam ="56892312455", categoria = "Carga", empresa = novaE2)
    config.db.session.add(novoV1)
    config.db.session.add(novoV2)
    config.db.session.commit()
    '''
    todosVeiculos = config.db.session.query(Veiculo).all()
    for meusVeiculos in todosVeiculos:
        print(meusVeiculos)
    for vJson in todosVeiculos:
        print(vJson.json())
    '''
    print("Teste Veículo")
    print(novoV1)
    print(novoV2.json())
    print("--------------------------------------------------------------------------")

    #Teste Habilitação
    novaH1 = Habilitacao(numero = "12345678", categoria = "AB", dataValidade = "25/05/2025")
    novaH2 = Habilitacao(numero = "98765432", categoria = "D", dataValidade = "06/12/2024")
    config.db.session.add(novaH1)
    config.db.session.add(novaH2)
    config.db.session.commit()
    print("Teste Habilitação")
    print(novaH1)
    print(novaH2.json())
    print("--------------------------------------------------------------------------")

    #Teste Motorista
    novoM1 = Motorista(nome = "Mesquita", cpf = "36985214", dataNascimento = "25/12/1989", idade = "31", \
    endereco = "rua wippel", habilitacao = novaH1)
    novoM2 = Motorista(nome = "Antonio", cpf = "14785296", dataNascimento = "12/08/1988", idade = "32", \
    endereco = "rua são joão", habilitacao = novaH2) 
    config.db.session.add(novoM1)
    config.db.session.add(novoM2)
    config.db.session.commit()
    print("Teste Motorista")
    print(novoM1)
    print(novoM2.json())
    print("--------------------------------------------------------------------------")

    #Teste TipoCombustível
    novoTc1 = TipoCombustivel(tipo = "gasolina", valor = "5,09")
    novoTc2 = TipoCombustivel(tipo = "diesel", valor = "3,89")
    config.db.session.add(novoTc1)
    config.db.session.add(novoTc2)
    config.db.session.commit()
    print("Teste TipoCombustível")
    print(novoTc1)
    print(novoTc2.json())
    print("--------------------------------------------------------------------------")

    #Teste Abastecimento
    valorAbastecimento = Abastecimento.calcularValorTotal
    novoAb1 = Abastecimento(posto = "Gasosa Barata", tipoCombustivel = novoTc1, quantidade = "50", valortotal = "300", quilometragem = "65023", data = "25/08/2020", veiculo = novoV1, motorista = novoM1)
    config.db.session.add(novoAb1)
    config.db.session.commit()
    print("Teste Abastecimento")
    print(novoAb1)
    print(novoAb1.json())
    print("--------------------------------------------------------------------------")



