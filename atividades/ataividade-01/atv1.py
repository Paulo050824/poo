class Aluno:
    def __init__(self, nome, curso, idade):
        self.nome = nome
        self.curso = curso
        self.idade = idade
    def __str__(self):
        return f"|Nome: {self.nome} \n|Curso: {self.curso} \n|Idade: {self.idade} anos\n-------------------------------------------------"



aluno1 = Aluno("João", "Programador de sistemas", 18)
aluno2 = Aluno("Ana", "Programador web", 16)
aluno3 = Aluno("Poliana", "Programador web", 17)

print(aluno1)
print(aluno2)
print(aluno3)
        