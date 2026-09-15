class Livro:
    livros = []
    def __init__(self,titulo,autor,ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self._disponivel = True
        Livro.livros.append(self)
    def __str__(self):
        return f"|Titulo: {self.titulo} \n|Autor: {self.autor} \n|Ano: {self.ano} \n|Status: {self.ativo}\n-----------------------------------------------------------"
    @property
    def ativo(self):
        return 'Disponivel' if self._disponivel else 'Indisponivel'
    
    def emprestar(self):
        self._disponivel = not self._disponivel
    def devolver(self):
        if self._disponivel == False:
            self._disponivel = True
        else:
            return self._disponivel






livro_1 = Livro("Dom Casmurro", "Machado de Assis",1899 )
livro_2 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)
livro_3 = Livro("1984", "George Orwell", 1949)
livro_4 = Livro("O Hobbit", "J.R.R. Tolkien", 1937)
livro_5 = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997)
Livro.emprestar(livro_3)
Livro.emprestar(livro_5)
Livro.emprestar(livro_1)

print(livro_1)
print(livro_2)
print(livro_3)
print(livro_4)
print(livro_5)