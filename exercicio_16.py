def exercicio_16():
    cigarros_por_dia = int(input('Quantidade de cigarros fumados por dia: '))
    anos_fumando = int(input('Há quantos anos você fuma? '))
    total_cigarros = cigarros_por_dia * 365 * anos_fumando
    total_minutos_perdidos = total_cigarros * 10
    dias_perdidos = total_minutos_perdidos / 1440
    print('-' * 40)
    print(f'Estima-se que você já perdeu {dias_perdidos:.2f} dias de vida devido ao fumo.')