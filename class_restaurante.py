from class_avaliacao import avalicao

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria
        self._cardapio = []
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    def listar_restaurantes(cls):
        print(f"{'Nome do Restaurante'.ljust(25)}| {'Categoria'.ljust(25)} | {'Avaliações'.ljust(25)}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante._avaliacoes}')

    def receber_avaliacao(self, nome, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(nome,nota)
            self._avaliacoes.append(avaliacao)


    
    





bistro_paris = Restaurante('Bistrô Paris', 'Francesa')
sushi_zen = Restaurante('Sushi Zen', 'Japonesa')
cantina_roma = Restaurante('Cantina Roma', 'Italiana')
burger_king = Restaurante('Burger King', 'Fast Food')
taco_loco = Restaurante('Taco Loco', 'Mexicana')
churrascaria_sul = Restaurante('Churrascaria Pampa', 'Carnes')
vegan_delight = Restaurante('Vegan Delight', 'Vegetariana')
padaria_central = Restaurante('Padaria Central', 'Panificadora')
cafe_amargo = Restaurante('Café Amargo', 'Cafeteria')
sorveteria_gelo = Restaurante('Sorveteria Gelo', 'Sobremesas')
mar_aberto = Restaurante('Mar Aberto', 'Frutos do Mar')
kebab_house = Restaurante('Kebab House', 'Árabe')
thai_spicy = Restaurante('Thai Spicy', 'Tailandesa')
doceria_fina = Restaurante('Doceria Fina', 'Confeitaria')
boteco_esquina = Restaurante('Boteco da Esquina', 'Bar e Petiscos')

Restaurante.listar_restaurantes(Restaurante)