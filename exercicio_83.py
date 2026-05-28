def exercicio_83():
    import  random
    vetordesordenado = []
    
    for i in range(20):
        numero = random.randint(0, 99)
        vetordesordenado.append(numero)
        
    print('Vetor desordenado:', vetordesordenado)
    
    vetorOrdenado = sorted(vetordesordenado)
    print('Vetor ordenado:', vetorOrdenado)