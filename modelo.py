import config


class Veiculo(config.db.Model):
    id = config.db.Column(config.db.Integer, primary_key=True)
    marca = config.db.Column(config.db.String(254)) # ex = Chevrolet
    nomeDescricao = config.db.Column(config.db.String(254)) # ex = gol city
    anoModelo = config.db.Column(config.db.String(254)) # ex = 2013/2014
    cor = config.db.Column(config.db.String(254)) # ex = azul
    placa = config.db.Column(config.db.String(254)) # ex = FjK2520
    renavam = config.db.Column(config.db.Integer)
    categoria = config.db.Column(config.db.String(254)) # ex = Ultilitário, Passeio, carga
    def __str__(self) -> str:
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

    if config.os.path.exists(config.arquivobd):
        config.os.remove(config.arquivobd)
    config.db.create_all()

    novo = Veiculo(marca = "vw", nomeDescricao = "golf gti", anoModelo="2015/2016", \
    cor = "cinza", placa = "aaa1111", renavam ="12345678965", categoria = "passeio")

    novo2 = Veiculo(marca = "hk", nomeDescricao = "Scania", anoModelo="2015/2016", \
    cor = "cinza", placa = "aaa1111", renavam ="12345678965", categoria = "Carga")


    config.db.session.add(novo)
    config.db.session.add(novo2)
    config.db.session.commit()
    todosVeiculos = config.db.session.query(Veiculo).all()


    for meusVeiculos in todosVeiculos:
        print(meusVeiculos)
    for vJson in todosVeiculos:
        print(vJson.json())


