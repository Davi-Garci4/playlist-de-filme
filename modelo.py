class Programa:           # Essa é a classe mãe (herança) do filme e serie.
    def __init__(self, nome, ano):   #através do init, que é uma função construtora adicionei os atributos "nome e ano"
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property                # Aqui eu utilizei o property para criar o retorno de likes
    def likes(self):
        return self._likes

    def dar_likes(self):    #aqui é uma funçaõ de dar likes em um filme ou serie
        self._likes += 1

    @property            #Aqui eu retorno os nomes
    def nome(self):
        return self._nome

    @nome.setter          #Aqui eu mudo os nomes
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):      # Aqui eu estou utilizando a função "__str__" para me retornar o objeto em forma de string
        return f" {self._nome} - {self.ano} - {self._likes} Likes"



class Filme (Programa):      #Criação da classe filme, entre parênteses esta a classe mãe utilizada como base
    def __init__(self, nome, ano, duracao,):
        super().__init__(nome, ano)     # Aqui eu utilizo o "super()" para chamar a classe mãe e o "__init__", para utilizar os atributos da classe mãe
        self.duracao = duracao

    def __str__(self):
        return f" {self._nome} - {self.ano} - {self.duracao} minutos -  {self._likes} Likes"


class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f" {self._nome} - {self.ano} - {self.temporada} Temporadas -  {self._likes} Likes"

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):       #Aqui o "__getitem__" esta trazendo algumas noções de sequência ao objeto e alguns métodos como "for" e "in".
        return self._programas[item]

    def ver_programas(self):
        for programas in self._programas:
            print(programas)


    @property
    def tamanho(self):
        return len(self._programas)




