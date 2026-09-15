from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato
from models.cardapio.sobremesas import Sobremesas


la_mafia = Restaurante("La Mafia", "rua açai, N:401", "Italiana/Japonesa", 7) 
mada = Restaurante("Mada pizzaria", "Rua Atilio, N:209", "Italiana", 4)
steve_pizza = Restaurante("Steve Pizza", "Rua Doutor Murici, N:70" ,"Porções", 3)
Restaurante.ativar(la_mafia)
la_mafia.receber_avaliacao("Heron", 5.0)
la_mafia.receber_avaliacao("Paulo", 5.0)

macarrao = Prato("Macarrão a bolonhesa, com strogonoff", 86.99, "Macarrão muito saboroso feito com muito amor")
child_fortnite = Bebida("Child azul, alcoolico", 15.99, "750ML")
pastel = Prato("Pastel de carne de cachorro", 15.99, "Pastel saboroso com carne de cachorro e muita maconha, (vindo da CHINA)")
sorvete = Sobremesas("Creme de Esgoto", 9.99, "Sorvete de chocolate com gosto de água ")

la_mafia.adicionar_ao_cardapio(macarrao)
la_mafia.adicionar_ao_cardapio(child_fortnite)
la_mafia.adicionar_ao_cardapio(pastel)
la_mafia.adicionar_ao_cardapio(sorvete)



def main():
    Restaurante.listar_restaurante()
    la_mafia.exibir_cardapio

if __name__ == "__main__":
    main()