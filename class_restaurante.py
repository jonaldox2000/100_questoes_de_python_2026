class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.cardapio = []
        self.reserva = 10

alfredus = Restaurante('Alfredus', 'Pizzaria')


print(alfredus.categoria)