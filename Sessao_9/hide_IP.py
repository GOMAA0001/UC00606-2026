"""Função para mascarar endereços IP."""


def mask_ip(ip: str) -> str:
    """Mascara um IP no formato a.b.c.d como a.***.***.d.

    Parâmetros:
        ip (str): endereço IP em texto.

    Retorno:
        str: IP mascarado, ou "IP inválido" se o formato não for a.b.c.d.
    """
    # Divide o IP pelos pontos
    partes = ip.split(".")

    # Um IP válido tem exatamente 4 partes
    if len(partes) == 4:
        return partes[0] + ".***.***." + partes[3]
    else:
        return "IP inválido"