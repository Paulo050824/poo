class Produto:
    produtos = []
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.disponivel = False
    def __str__(self): 
        return f"Produto: {self.nome} - R${self.preco}"
    def aplicar_desconto(self):
        desconto = float(input("Digite o valor do desconto: R$"))
        self.preco = self.preco - desconto 

produto01 = Produto("Detergente", 12.99)
produto02 = Produto("Fralda", 25.95)
produto03 = Produto("Barra de chocolate", 5.99)

Produto.aplicar_desconto(produto01)
print(produto01)
print(produto02)
print(produto03)




