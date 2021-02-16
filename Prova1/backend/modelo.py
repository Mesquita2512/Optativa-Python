import config



#Empresa
class Empresa(config.db.Model):
    id = config.db.Column(config.db.Integer, primary_key=True)
    nome = config.db.Column(config.db.String(254)) # ex = Chevrolet
    cnpj = config.db.Column(config.db.String(254)) # ex = gol city
    endereco = config.db.Column(config.db.String(254)) # ex = 2013/2014
    telefone = config.db.Column(config.db.String(254)) # ex = azul
    

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
               # o str aciona o __str__ da classe Pessoa

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

if __name__ == "__main__":

    if config.os.path.exists(config.arquivobd):
        config.os.remove(config.arquivobd)
    config.db.create_all()

    nova = Empresa(nome = "transportes suleicarias", cnpj = "555555555", endereco="rua das maricas", \
    telefone = "583696369")

    novob = Empresa(nome = "meredes transportadora", cnpj = "222222222", endereco="rua das flores", \
    telefone = "4785858585")

    config.db.session.add(nova)
    config.db.session.add(novob)
    config.db.session.commit()
    print(nova)
    print(novob)

    novo2 = Veiculo(marca = "hk", nomeDescricao = "Scania", anoModelo="2015/2016", \
    cor = "cinza", placa = "aaa1111", renavam ="12345678965", categoria = "Carga", empresa = nova)

    novo3 = Veiculo(marca = "Scania", nomeDescricao = "Scania", anoModelo="2016/2016", \
    cor = "preto", placa = "aaa1123", renavam ="56892312455", categoria = "Carga", empresa = novob)

    
    config.db.session.add(novo2)
    config.db.session.add(novo3)
    config.db.session.commit()
    todosVeiculos = config.db.session.query(Veiculo).all()


    for meusVeiculos in todosVeiculos:
        print(meusVeiculos)
    for vJson in todosVeiculos:
        print(vJson.json())
