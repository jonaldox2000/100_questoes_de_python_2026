def exercicio_31():
    import random
    
    itens = ['Pedra', 'Papel', 'Tesoura']
    
    usuario = int(input('0-Pedra, 1-Papel, 2-Tesoura: '))
    pc = random.randint(0, 2)
    
    print(f'Você: {itens[usuario]} vs PC: {itens[pc]}')
    
    if usuario == pc:
        print('Empate!')
    elif (usuario - pc) % 3 == 1:
        print('Você venceu!')
    else:
        print('PC venceu!')
    
