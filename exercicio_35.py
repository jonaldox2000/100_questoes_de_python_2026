def exercicio_35():
    carro = input('Normal ou luxo:')
    dias = float(input('Quantos dias de aluguel:'))
    km = float(input('Quantos KM foram percorridos:'))
    
    if carro == 'normal':
        aluguel = dias * 90
        if km <= 100:
            custo_km = km * 0.20
        else:
            custo_km = km * 0.10
            
            
    else:
        aluguel = 150 * dias
        if km <= 200:
            custo_km = km * 0.30
        else:
            custo_km = km * 0.25
            
    total = aluguel + custo_km
    print('Total a pagar:R$', total)