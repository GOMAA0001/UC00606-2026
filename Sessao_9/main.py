"""Programa principal: coordena as funções dos outros ficheiros."""

from hide_IP import mask_ip
from check_email import is_corporate_email
from password import hash_password,check_password


def main():
    """Pede password, email e IP ao utilizador e mostra os resultados.

    Mostra o hash SHA-256 da password, se o email é corporativo
    e o IP mascarado. Todas as variáveis são locais.
    """
    """
    # Dados introduzidos pelo utilizador (variáveis locais)
    pwd = input("Password: ")
    email = input("Email: ")
    ip = input("IP: ")

    # Resultados
    print("Hash da password:", hash_password(pwd))
    print("Email corporativo:", is_corporate_email(email))
    print("IP mascarado:", mask_ip(ip))
    """

    """
    Este Codígo é um sign in simples

    se possivel importar time

    Lê o IP do utilizador e o Email.
    Lê e Cria um hash da palavra passe do utilizador.
    Pedir para o utilizador escrever a mesma Palavra-Passe.

    Verifica se IP é valído.
    Verifica se o Email é da Empresa.
    Verifica se os hash das Palavra-Passes são iguais.

    Se tudo estiver certo informa o utilizador que a conta foi criada con sucesso.
    """
    masked_ip = mask_ip(input("\nEscreva o seu IP: "))
    email = input("\nEscreva o seu Email: ")
    password_hashed = hash_password(input("\nEscreva a sua Palavra-Passe: "))
    same_hash = check_password(input("\nComfirme a sua Palavra-Passe: "),password_hashed)

    if(masked_ip == "IP inválido"):
        print("O IP esta inválido")
    elif(is_corporate_email(email)==False):
        print("O Email é inválido")
    elif(not same_hash):
        print("As Palavra-Passes não correspondem")
    else:
        print("Conta criada com sucesso.\n" \
        f"IP: {masked_ip}\n" \
        f"Email: {email}")

main()