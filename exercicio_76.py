def exercicio_76():
    import random
    
    vetor = [ ]
    
    for numero in range(7):
        numero_aleatorio = random.randint(0,100)
        vetor.append(numero_aleatorio)
        
    print(vetor)