def exercicio_98():
    def SuperSomador(inicio, fim):
        soma_total = 0
        atual = inicio
        
        
        while atual <= fim:
            soma_total += atual 
            atual += 1          
            
        return soma_total 
    
    
    n1 = int(input('Digite o valor inicial do intervalo: '))
    n2 = int(input('Digite o valor final do intervalo: '))
    
    resultado = SuperSomador(n1, n2)
    
    
    print(f'A soma de todos os valores no intervalo de {n1} até {n2} é: {resultado}')