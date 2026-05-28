def exercicio_36():
    horas = float(input('Quantas horas de atividade física você fez este mês:'))
    
    pontos = 0
    
    if horas <= 10:
        pontos = horas * 2
    elif horas <= 20:
        pontos = horas * 5
    else:
        pontos = horas * 10
    
    faturamento = pontos * 0.05
    
    print('-' * 30)
    print(f'Total de horas:{horas}h')
    print(f'Pontos acumulados:{pontos} pts')
    print(f'Dinheiro ganho: R$ {faturamento:.2f}')
    print('-' * 30)
        