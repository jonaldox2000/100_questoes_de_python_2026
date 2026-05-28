def exercicio_58():
    soma = 0
    contador = 0
    
    while True:
        idade = int(input("Digite a idade (999 para parar): "))
        
        if idade == 999:
            break
        
        soma += idade
        contador += 1
    
    if contador > 0:
        media = soma / contador
    else:
        media = 0
    
    print(f'Quantidade de alunos:" {contador}')
    print(f'Média de idade:" {media:.2f}')