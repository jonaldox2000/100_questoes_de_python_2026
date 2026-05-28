def exercicio_9():
    real = float(input('Quanto dinheiro você tem na carteira? '))
    cotacao = float(input('Qual a cotação atual do dólar? '))
    dolar = real / cotacao
    print(f'Com R$ {real:.2f}, você pode comprar US$ {dolar:.2f}')