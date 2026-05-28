def exercicio_100():
    def Media(num_1, num_2):
        return (num_1 + num_2) / 2
    
    def Situacao(media_aluno):
        if media_aluno >= 7.0:
            return 'APROVADO'
        elif 5.0 <= media_aluno < 7.0:
            return ' em RECUPERAÇÃO'
        else:
            return 'REPROVADO'
        
        
    n1 = float(input('Digite o primeira nota: '))
    n2 = float(input('Digite o segunda nota: '))
    
    media_final = Media(n1, n2)
    
    status_aluno = Situacao(media_final)
    
    
    print('-' * 30)
    print(f'Média do aluno: {media_final:.1f}')
    print(f'Situação do aluno: {status_aluno}')
    print('-' * 30)
     
