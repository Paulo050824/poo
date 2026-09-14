from models.avaliacao import Avaliacao
from models.cardapio.itemcardapio import ItemCardapio
class Restaurante:
    restaurantes = []
    # lista
    def __init__(self, nome_restaurante, localizacao,tipo_de_comida
         ,quantidade_funcionarios,):
        # inicializa nosso restaurante ou qualquer coisa que colocarmo como: livraria, restaurantes, roupas e etc...
        self.nome_restaurante = nome_restaurante
        self.localizacao = localizacao
        self.tipo_de_comida = tipo_de_comida
        self.quantidade_funcionarios = quantidade_funcionarios
        self._status = False
        self._avaliacao = []
        self._cardipio = []
        Restaurante.restaurantes.append(self)

    def __str__(self): 
    # retornara somente a mensagem escrita dentro do return
        # return self.nome
        return f"|nome: {self.nome_restaurante} \n|Rua: {self.localizacao} \n|tipo de comida: {self.tipo_de_comida} \n|Quantidade de funcionarios: {self.quantidade_funcionarios} \n|Status: {self.ativo} \n|Avaliação: {self.media}"
    # def listar_restaurantes():
    @property
    def ativo(self):
        return 'aberto' if self._status else 'fechado'
    @property
    def media(self):
        if not self._avaliacao:
            return 0
        notas_somadas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quant_notas = len(self._avaliacao)
        media_total = round(notas_somadas/quant_notas, 1)
        return media_total
    @property
    def exibir_cardapio(self):
        print(f"Cardápio do restaurante: {self.nome_restaurante}")
        for i,item in enumerate(self._cardipio,start=1):
            if hasattr(item,'descricao'):
                mensagem_prato = f"{i}.|Nome: {item._nome} \n|Preço: {item._preco} \n|Descrição: {item.descricao}"
                print(mensagem_prato)
            elif hasattr(item,'tamanho'):
                mensagem_bebida = f"{i}.|Nome: {item._nome} \n|Preço: {item._preco} \n|Tamanho: {item.tamanho}"
                print(mensagem_bebida)
            else:
                mensagem_sobremesas = f"{i}.|Nome: {item._nome} \n|Preço: {item._preco} \n|Sabor: {item.sabor}"
                print(mensagem_sobremesas)

    @classmethod
    def listar_restaurante(cls):
        for restaurante in cls.restaurantes:
            print(f"|Nome: {restaurante.nome_restaurante} \n|Rua: {restaurante.localizacao} \n|Tipo de Comida: {restaurante.tipo_de_comida} \n|Quantidade de Funcionários: {str(restaurante.quantidade_funcionarios)} \n|Status: {restaurante.ativo} \n|Avalição: {restaurante.media} \n ----------------------------------------------------------")

    def ativar(self):
        self._status = not self._status

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    def adicionar_ao_cardapio(self,item):
        if isinstance(item, ItemCardapio):
            self._cardipio.append(item)