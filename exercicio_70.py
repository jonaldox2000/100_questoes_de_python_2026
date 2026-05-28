def exercicio_70():
    inicio = proximo = 1
    
    for contagem in range(10):
        print(proximo, end=' ')
        soma = inicio + proximo
        proximo = inicio
        inicio = soma