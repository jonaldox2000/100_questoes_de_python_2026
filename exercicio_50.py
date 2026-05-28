def exercicio_50():
    import random
    numero = 0
    menor_que_cinco = 0
    divisivel_por_tres = 0
    
    while numero < 20:
        valor = random.randint(0, 10)
        print(valor, end=' ')
        
        if valor > 5:
            menor_que_cinco += 1
            
        if valor % 3 == 0:
            divisivel_por_tres += 1
            numero += 1
    print()
    print(f'{menor_que_cinco} são maior que 5')
    print(f'{divisivel_por_tres} são divivel por 3')
        
        
        
        
            
            
