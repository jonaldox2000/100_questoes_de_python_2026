def exercicio_62():
    pessoas_21_mais = 0
    quantas_idades = 0
    soma_idade = 0
    continuar ='S'
    contador = 0
    
    while continuar == 'S':
        idade = int(input('Digite a idade: '))
        
        soma_idade += idade
        
        contador += 1
        quantas_idades += 1
       
        if idade >= 21:
            pessoas_21_mais += 1
            
     
        continuar = input('Quer continuar? (S/N): ').upper()
        
    if contador > 0:
        media = soma_idade / contador
    else:
        media = 0
        
    print(f'Foram {quantas_idades} idades digitadas')
    print(f'A média foi {media} entre idades digitadas')
    print(f'São {pessoas_21_mais} pessoas que tem 21 anos ou mais')
        