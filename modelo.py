class Filme:
    def __init__(self, nome, ano, duracao,):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    def dar_likes(self):
        self.likes += 1

class Serie:
    def __init__(self, nome, ano, temporada):
        self.nome = nome.title()
        self.ano = ano
        self.temporada = temporada
        self.likes = 0

    def dar_likes(self):
            self.likes += 1