import random
import string

def gerar_senha(tamanho=12):
    # Define os caracteres que a senha pode ter
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Gera a senha escolhendo caracteres aleatórios
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Execução do programa no terminal
print("--- GERADOR DE SENHAS SEGUIRAS ---")
try:
    comprimento = int(input("Digite o tamanho da senha desejada (ex: 12): "))
    if comprimento < 4:
        print("Para sua segurança, a senha deve ter pelo menos 4 caracteres.")
    else:
        senha_gerada = gerar_senha(comprimento)
        print(f"\nSua nova senha é: {senha_gerada}")
except ValueError:
    print("Por favor, digite um número válido.")
