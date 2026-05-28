def exercicio_27():
    n1 = float(input('Primeira nota:'))
    n2 = float(input('Segunda nota:'))
    
    media = n1 + n2
    
    if media >= 7.0:
        print('Você foi Aprovado')
    
    elif media >= 5:
        print('Você ficou de Recuperação')
        
        
    else:
        print('Você foi Reprovado')
    
