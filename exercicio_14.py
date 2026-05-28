def exercicio_14():
    km_percorridos = float(input('Informe a quantidade de Km percorridos: '))
    dias_alugados = int(input('Informe a quantidade de dias de aluguel: '))
    custo_dias = dias_alugados * 90
    custo_km = km_percorridos * 0.20
    preco_total = custo_dias + custo_km
    print(f'O custo fixo por dias foi R${custo_dias:.2f}')
    print(f'O custo por quilometragem foi R${custo_km:.2f}')
    print(f'O valor total a pagar pelo aluguel é R${preco_total:.2f}')