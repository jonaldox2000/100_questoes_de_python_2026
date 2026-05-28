def exercicio_82():
    notas = []
    soma = 0
    
    
    for numero in range(10):
        nota = float(input(f'Digite a nota {numero+1}: '))
        notas.append(nota)
        soma = soma + nota
    
    
    media = soma / 10
    
    
    maior = notas[0]
    for nota in notas:
        if nota > maior:
            maior = nota
    
    
    acima_media = 0
    for nota in notas:
        if nota > media:
            acima_media = acima_media + 1
    
    print(' Média da turma:', media)
    print('Alunos acima da média:', acima_media)
    print('Maior nota:', maior)
    
    
    print('Posições da maior nota:', end=' ')
    for numero in range(10):
        if notas[numero] == maior:
            print(numero + 1, end=' ')
