import config


class Empresa(config.db.model):
    id = config.db.Column(config.db.Integer, primary_key=True)
    nome = config.db.Column(config.db.String(254))
    cnpj = config.db.Column(config.db.Integer)
    endereco = config.db.Column(config.db.String(254))
    telefone = config.db.Column(config.db.Integer)
    def __str__(self) -> str:
        return str(self.id) + ", " + self.nome + ", " + str(self.cnpj) + ", " + self.endereco + ", " + str(self.telefone)
    
    def json(self):
        return{
            "id" : self.id,
            "nome" : self.nome,
            "cnpj" : self.cnpj,
            "endereco" : self.endereco,
            "telefone" : self.telefone
        }

if __name__ == "__main__":

    if config.os.path.exists(config.arquivobd):
        config.os.remove(config.arquivobd)
    config.db.create_all()

    nova = Empresa(nome = "transportes FdK", cnpj = "5562626652", endereco="rua das maricas, 25, blumenau-sc", telefone = "47-698589742") 
    novb = Empresa(nome = "transportes los", cnpj = "5526000652", endereco="rua das maricas, 21, blumenau-sc", telefone = "47-898509742") 
    novc = Empresa(nome = "transportes dfr", cnpj = "5566156652", endereco="rua das maricas, 85, blumenau-sc", telefone = "47-398589741") 
    novd = Empresa(nome = "transportes lkw", cnpj = "5002626652", endereco="rua das maricas, 60, blumenau-sc", telefone = "47-598589740")   

    config.db.session.add(nova)
    config.db.session.add(novb)
    config.db.session.add(novc)
    config.db.session.add(novd)
    config.db.session.commit()
    todasEmpresas = config.db.session.query(Empresa).all()


    for empresas in todasEmpresas:
            print(empresas)
    for vJson in todasEmpresas:
            print(vJson.json())