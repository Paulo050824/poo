class Mercado_Livre:
    produtos = []
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.disponivel = False
        Mercado_Livre.produtos.append(self)
    def __str__(self):
        return f"Produto: {self.nome} \n|Preço:{self.preco}\n|Status: {self.disponivel} \n------------------------------------------"
    def aplicar_desconto(self, desconto):
        self.desconto = desconto
        self.preco -= desconto
    def listar_produtos():
        for produto in Mercado_Livre.produtos:
            print(f"Produto: {produto.nome}| R${produto.preco} | Status: {produto.disponivel}")



aerofolio_palio = Mercado_Livre("Aerofolio", 273.99)
body_kit = Mercado_Livre("Body quit", 1700)
roda_palio = Mercado_Livre("Roda", 3189.99)

Mercado_Livre.aplicar_desconto(body_kit, 250.99)
Mercado_Livre.aplicar_desconto(roda_palio, 658.99)

Mercado_Livre.listar_produtos()
# print(aerofolio_palio)
# print(body_kit)
# print(roda_palio)

