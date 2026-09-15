class Filme:
    filmes = []
    def __init__(self, titulo, genero, ano):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        Filme.filmes.append(self)
    def __str__(self):
        return f"|Titulo: {self.titulo} \n|Genero>: {self.genero} \n|Ano: {self.ano}"

    @classmethod
    def listar_filmes(cls):
        for filme in cls.filmes:
            print(f"|Titulo:{filme.titulo} \n|Genêro: {filme.genero} \n|Ano: {filme.ano}\n------------------------------------------------")


filme_1 = Filme("Monstros S.A", "Animação", 2001)
filme_2 = Filme("O Poderoso Chefão", "Crime", 1972)
filme_3 = Filme("Interestelar", "Ficção Científica", 2014)
filme_4 = Filme("Invocação do Mal", "Terror", 2013)
filme_5 = Filme("Forrest Gump", "Drama", 1994)
filme_6 = Filme("As Branquelas", "Comédia", 2004)
filme_7 = Filme("Homem-Aranha: Sem Volta Para Casa", "Ação", 2021)

Filme.listar_filmes()