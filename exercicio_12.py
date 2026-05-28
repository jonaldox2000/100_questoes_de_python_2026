def exercicio_12():
    Preço = float(input('Digite o preço do produto:'))
    Desconto = Preço * 0.05
    promoção = Preço - Desconto
    print(f"O produto que custava R$ {Preço:.2f}, com 5% de desconto,")
    print(f"passará a custar R$ {promoção:.2f}.")