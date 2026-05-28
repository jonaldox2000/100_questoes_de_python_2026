def exercicio_10():
    L = float(input('Largura da parede em metros:'))
    H = float(input('Altura da parede em metros:'))
    A = L * H
    TN = A / 2
    print(f'A parede tem {L}m x {A}m.')
    print(f'Área total: {A:.2f}m²')
    print(f'Quantidade de tinta: {TN:.2f} litros')