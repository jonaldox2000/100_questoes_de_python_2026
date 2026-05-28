def exercicio_96():
    def media(num_1, num_2):
        soma = num_1 + num_2
        media = soma / 2
        
        return media
    n1 = float(input('Digite o primeira nota: '))
    n2 = float(input('Digite o segunda nota: '))
    
    print(media(n1, n2))