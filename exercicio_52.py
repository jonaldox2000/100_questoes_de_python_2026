def exercicio_52():
    validador = 0
    soma_idades = 0
    maior_18 = 0
    menor_5 = 0
    maior_idade = 0
    
    while validador < 10:
        idade = int(input('Qual a sua idade: '))
        soma_idades = soma_idades + idade
        
        if validador == 0:
            maior_idade = idade
        if idade > 18:
            maior_18 += 1
        if idade < 5:
            menor_5 += 1
        validador += 1
    media = soma_idades / 10
    print(f'Media das idades:{media}')
    print(f'{maior_18} pessoas tem mais de 18 anos')
    print(f'{menor_5} pessoas tem menos de 5 anos')
    print(f'A maior idade foi {maior_idade}')
        
        
    
        
    
        
        