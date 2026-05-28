def exercicio_94():
    
    def Fibonacci(termos):
        t1 = 1
        t2 = 1
        
        print('Sequência: ', end="")
        
        contador = 1
        
        while contador <= termos:
            print(f'{t1} >> ', end=' ')
            
            proximo = t1 + t2
            
            t1 = t2
            t2 = proximo
            
            contador += 1
            
        print('FIM')
    
    num_termos = int(input("Quantos termos voçê quer ver: "))
    Fibonacci(num_termos)