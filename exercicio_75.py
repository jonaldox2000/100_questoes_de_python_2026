def exercicio_75():
    vetor_fibonacci = [ ]
    
    vetor_fibonacci.append(1)
    vetor_fibonacci.append(1)
    
    for numero in range(2, 16):
        proximo_elemento = vetor_fibonacci[numero-1] + vetor_fibonacci[numero-2]
        vetor_fibonacci.append(proximo_elemento)
    
    print(vetor_fibonacci)