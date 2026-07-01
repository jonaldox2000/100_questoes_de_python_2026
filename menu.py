
import os
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


print("""

██████╗░███████╗░██████╗████████╗░█████╗░██╗░░░██╗██████╗░░█████╗░███╗░░██╗████████╗███████╗
██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██║░░░██║██╔══██╗██╔══██╗████╗░██║╚══██╔══╝██╔════╝
██████╔╝█████╗░░╚█████╗░░░░██║░░░███████║██║░░░██║██████╔╝███████║██╔██╗██║░░░██║░░░█████╗░░
██╔══██╗██╔══╝░░░╚═══██╗░░░██║░░░██╔══██║██║░░░██║██╔══██╗██╔══██║██║╚████║░░░██║░░░██╔══╝░░
██║░░██║███████╗██████╔╝░░░██║░░░██║░░██║╚██████╔╝██║░░██║██║░░██║██║░╚███║░░░██║░░░███████╗
╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝ """)








def menu():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alternar estado do restaurante")
    print("4. Adicionar avaliação")
    print("5. Adicionar item ao cardápio")
    print("6. Exibir cardápio")
    print("7. Sair")

    int(input('Escolha uma opção:'))

def cadastrar_restaurante():
    print("\n" + "="*30)
    print("CADASTRAR NOVO RESTAURANTE")
    print("="*30)

    nome = input("Digite o nome do restaurante: ").strip()
    categoria = input("Digite a categoria do restaurante (ex: Italiana, Japonesa): ").strip()
    if nome and categoria:
        restaurantes.append({"nome": nome, "categoria": categoria, "ativo": False, "avaliacoes": [], "cardapio": []})
        print("Cadastrado com sucesso!")
                  
                  
def listar_restaurantes():
    print("\n=== LISTA ===")
    if not restaurantes:
        print("Nenhum restaurante cadastrado.")
    for i, r in enumerate(restaurantes, 1):
        status = "Ativo" if r["ativo"] else "Inativo"
        print(f"{i}. {r['nome']} ({r['categoria']}) - [{status}]")


    