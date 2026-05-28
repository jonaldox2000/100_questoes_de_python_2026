def exercicio_60():
    maior_idade = 0
    nome_mais_velho = ''
    
    menor_idade_mulher = 0
    nome_mulher_jovem = ''
    primeira_mulher = True
    
    soma_idade = 0
    homens_30 = 0
    mulheres_18 = 0
    
    contador = 0
    
    continuar = 'S'
    
    while continuar == 'S':
        nome = input('Digite seu nome: ')
        idade = int(input('Digite a idade: '))
        sexo = input('Digite o sexo (M/F): ').upper()
        
        soma_idade += idade
        contador += 1
        
        if idade > maior_idade:
            maior_idade = idade
            nome_mais_velho =  nome
        
        if sexo == 'F':
            if primeira_mulher:
                menor_mulher = idade
                nome_mulher_jovem = nome
                primeira_mulher = True
                
            else:
                if idade < menor_idade_mulher:
                   menor_idade_mulher = idade
                   nome_mulher_jovem = nome
        
        if sexo == 'M':
            if idade > 30:
                homens_30 += 1
        
        if sexo == 'F':
            if idade < 18:
                mulheres_18 += 1
        
        
        continuar = input('Quer continuar? (S/N): ').upper()
    
    if contador > 0:
        media = soma_idade / contador
    else:
        media = 0
    
    print(f'Nome da pessoa mais velha: {nome_mais_velho}')
    
    if primeira_mulher:
        print('Nenhuma mulher foi cadastrada')
    else:
        print(f'Nome da mulher mais jovem: {nome_mulher_jovem}')
    
    print(f'Media de idade: {media}')
    print(f'Homens com mais de 30 anos: {homens_30}')
    print(f'Mulheres com menos de 18 anos: {mulheres_18}')
