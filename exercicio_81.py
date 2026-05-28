def exercicio_81():
    idades = []
    
    for num in range(8):
        valor = int(input(f'Digite sua idade {num+1}: '))
        idades.append(valor)
    
    
    soma = 0
    maior = idades[0]  
    
    for num in range(8):
        soma = soma + idades[num]
        if idades[num] > maior:
            maior = idades[num]
    
    media = soma / 8
    
    
    print(' Média das idades:', media)
    
    print('Posições de quem tem mais de 25 anos:')
    for num in range(8):
        if idades[num] > 25:
            print(num)
    
    print('A maior idade digitada foi:', maior)
    
    print(' Posições onde a maior idade aparece:')
    for num in range(8):
        if idades[num] == maior:
            print(num)