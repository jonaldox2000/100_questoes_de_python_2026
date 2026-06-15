class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.cardapio = []
        Restaurante.restaurantes.append(self)
    def __str__(self):
    
        return f'{self.nome} | {self.categoria}'

alfredus = Restaurante('Alfredus', 'Pizzaria')

print(alfredus)