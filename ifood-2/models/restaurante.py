from models.avaliacao import Avaliacao

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

    @classmethod
    def listar_restaurante(cls):
        for restaurante in cls.restaurantes:
            print(f"|Nome: {restaurante.nome_restaurante} \n|Rua: {restaurante.localizacao} \n|Tipo de Comida: {restaurante.tipo_de_comida} \n|Quantidade de Funcionários: {str(restaurante.quantidade_funcionarios)} \n|Status: {restaurante.ativo} \n|Avalição: {restaurante.media} \n ----------------------------------------------------------")

    def ativar(self):
        self._status = not self._status

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)



    
