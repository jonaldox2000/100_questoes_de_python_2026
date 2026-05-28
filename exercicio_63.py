def exercicio_63():
    pares = 0
    soma = 0
    menor_valor = 99999999999999999
    continuar ='S'
    contador = 0
    
    while continuar == 'S':
        numero = int(input('Digite um número: '))
        
        soma += numero
        contador += 1
        resultado = numero % 2
        
        if numero < menor_valor:
            menor_valor = numero
            
        
        if resultado == 0:
            pares += 1
            
            
     
        continuar = input('Quer continuar? (S/N): ').upper()
        
    if contador > 0:
        media = soma / contador
    else:
        media = 0
    print(f'O somatório é {soma}')
    print(f'O menor valor é {menor_valor} digitado')
    print(f'A média foi {media} entre os valores digitados')
    print(f'São {pares} valores que são pares')
    
