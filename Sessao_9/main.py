"""Programa principal: coordena as funções dos outros ficheiros."""

from hide_IP import mask_ip
from check_email import is_corporate_email
from password import hash_password, check_password

def bool_to_text(valor: bool) -> str:
    """Converte um booleano em texto.

    Parâmetros:
        valor (bool): valor a analisar.

    Retorno:
        str: "Sim" se for True, "Não" se for False.
    """
    if (valor):
        return "Sim"
    else:
        return "Não"

def main():
    """Pede IP, email e password ao utilizador e mostra os resultados.

    Mostra o hash SHA-256 da password, se o email é corporativo
    e o IP mascarado. Todas as variáveis são locais.
    """
   
    # Dados introduzidos pelo utilizador (variáveis locais)
    masked_ip = mask_ip(input("\nEscreva o seu IP: "))
    email = input("\nEscreva o seu Email: ")
    password_hashed = hash_password(input("\nEscreva a sua Palavra-Passe: "))
    same_hash = check_password(input("\nConfirme a sua Palavra-Passe: "),password_hashed)

    # Resultados
    print("\nResultados:")
    print(f"\nIP mascarado: {masked_ip}")
    print(f"\nEmail corporativo: {bool_to_text(is_corporate_email(email))}")
    print(f"\nHash da password: {password_hashed}")
    print(f"\nA password é igual: {bool_to_text(same_hash)}")
   
main()


