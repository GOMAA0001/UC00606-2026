"""Função para verificar se um email pertence ao domínio corporativo."""


def is_corporate_email(email: str, dominio: str = "empresa.pt") -> bool:
    """Verifica se um email pertence ao domínio corporativo.

    Parâmetros:
        email (str): endereço de email.
        dominio (str): domínio corporativo (por omissão "empresa.pt").

    Retorno:
        bool: True se o email terminar em @dominio, False caso contrário.
    """
    return email.endswith("@" + dominio)