def exercicio_93():
    def Contador(inicio, fim, incremento):
        print('Contagem: ', end=' ')
        
        atual = inicio
    
        while atual <= fim:
            print(f'{atual} >> ', end=' ')
            atual += incremento 
            
        print('FIM')
    
    
    inicial = int(input('Digite o valor de início: '))
    final = int(input('Digite o valor de fim: '))
    inc = int(input('Digite o incremento: '))
    
    Contador(inicial, final, inc)