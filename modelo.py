class Programa:           # Essa é a classe mãe (herança) do filme e serie.
    def __init__(self, nome, ano):   #através do init, que é uma função construtora adicionei os atributos "nome e ano"
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property                # Aqui eu utilizei o property para criar o retorno de likes
    def likes(self):
        return self.__likes

    def dar_likes(self):    #aqui é uma funçaõ de dar likes em um filme ou serie
        self.__likes += 1

    @property            #Aqui eu retorno os nomes
    def nome(self):
        return self.__nome

    @nome.setter          #Aqui eu mudo os nomes
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


class Filme (Programa):      #Criação da classe filme, entre parênteses esta a classe mãe utilizada como base
    def __init__(self, nome, ano, duracao,):
        super().__init__(nome, ano)     # Aqui eu utilizo o "super()" para chamar a classe mãe e o "__init__", para utilizar os atributos da classe mãe
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada