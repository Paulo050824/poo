from models.restaurante import Restaurante


la_mafia = Restaurante("La Mafia", "rua açai, N:401", "Italiana", 7) 
mada = Restaurante("Mada pizzaria", "Rua Atilio, N:209", "Italiana", 4)
steve_pizza = Restaurante("Steve Pizza", "Rua Doutor Murici, N:70" ,"Porções", 3)
Restaurante.ativar(steve_pizza)
steve_pizza.receber_avaliacao("Heron", 2.5)
steve_pizza.receber_avaliacao("Paulo", 4.9)

def main():
    Restaurante.listar_restaurante()

if __name__ == "__main__":
    main()