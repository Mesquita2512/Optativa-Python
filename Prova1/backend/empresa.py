#Empresa criada e testada, ok!!!
import config


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
            "cor" : self.telefone
        }

if __name__ == "__main__":

    if config.os.path.exists(config.arquivobd):
        config.os.remove(config.arquivobd)
    config.db.create_all()

    novo = Empresa(nome = "transportes suleicarias", cnpj = "555555555", endereco="rua das maricas", \
    telefone = "583696369")

    novo1 = Empresa(nome = "meredes transportadora", cnpj = "222222222", endereco="rua das flores", \
    telefone = "4785858585")


    config.db.session.add(novo)
    config.db.session.add(novo1)
    
    config.db.session.commit()
    todosVeiculos = config.db.session.query(Empresa).all()


    for meusVeiculos in todosVeiculos:
        print(meusVeiculos)
    for vJson in todosVeiculos:
        print(vJson.json())
