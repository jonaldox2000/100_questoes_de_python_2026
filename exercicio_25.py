def exercicio_25():
    a = float(input('Primeiro segmento: '))
    b = float(input('Segundo segmento: '))
    c = float(input('Terceiro segmento: '))
    
    if a + b > c and a + c > b and b + c > a:
        print('\nOs segmentos acima PODEM FORMAR um triângulo!')
    else:
        print('\nOs segmentos acima NÃO PODEM FORMA um triângulo!')