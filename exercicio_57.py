def exercicio_57():
    total_homens = 0
    total_mulheres = 0 
    
    continuar = 'S' 
    
    while continuar == 'S':
        salario = float(input('Qual o seu salario: '))
        genero = input('Qual seu gênero M/F:')
        
        
        if genero == 'M':
            total_homens += salario
        if genero == 'F':
            total_mulheres += salario
        continuar = input('Quer continuar S/N: ')
    
    print(f'Total pago aos homens: {total_homens}')
    print(f'Total pago a mulheres: {total_mulheres}')
    
