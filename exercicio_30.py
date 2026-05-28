def exercicio_30():
    lado1 = float(input('Primeiro lado: '))
    lado2 = float(input('Segundo lado: '))
    lado3 = float(input('Terceiro lado: '))
    
    
    if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
        print('Os lados acima PODEM FORMAR um triângulo ', end='')
        
        
        if lado1 == lado2 == lado3:
            print('EQUILÁTERO!')
        elif lado1 != lado2 != lado3 != lado1:
            print('ESCALENO!')
        else:
            print('ISÓSCELES!')
            
    else:
        print('Os lados acima NÃO PODEM FORMAR um triângulo.')