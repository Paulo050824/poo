class Veiculo:
    carros = []

    def __init__(self, modelo, ano, marca, stoque):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self._vendido = False
        Veiculo.carros.append(self)
    def __str__(self):
        return f"|Marca: {self.marca} \n|Modelo: {self.modelo} \n|Ano: {self.ano} \n|Stoque: {self._stoque} \n|Status: {self.ativo} \n---------------------------------------------"
    @property
    def ativo(self):
        return 'vendido' if self._vendido else 'Disponivel' 
    
    def vender(self):
        self._vendido = not self._vendido


palio = Veiculo("Palio", 2008, "FIAT", )
gt3 = Veiculo("Porsche 911 GT3-RS", 2023, "Porsche", )
r34 = Veiculo("Nissan skyline GTR r34", 1999, "Nissan", )
Veiculo.vender(r34)
print(palio)
print(gt3)
print(r34)
