def exercicio_32():
    import random
    contador = 0
    escolha_computador = random.randint(1,10)
    
    while contador < 4:
    
        jogador = int(input('Digite um número em 1 e 10:'))
    
        if jogador == escolha_computador:
            print(f'Acertou! O computador também escolheu {escolha_computador}.')
            break
            
        else:
            print(f'Errou! O computador escolheu {escolha_computador} e você escolheu {jogador}.')
            contador += 1