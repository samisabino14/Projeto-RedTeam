""" enumeração de domínio Active Directory """

from ldap3 import Server, Connection, ALL
from core.utils import separate_domain

domain_parts = separate_domain()

def ad_connect(dc_ip: str, user: str, password: str):

    server = Server(dc_ip, get_info=ALL)

    """ tenta estabelecer uma conexão com o controlador de domínio usando as credenciais fornecidas """
    conn = Connection(server, user=user, password=password, auto_bind=True) # ****************************************

    return conn

def enumerate_users(conn: Connection) -> list[str]:
    """ função para enumerar os usuários do Active Directory usando a conexão LDAP estabelecida """

    domain_parts = separate_domain()

    """ pesquisa por todos os objetos do tipo 'user' no Active Directory e retorna seus nomes de usuário (sAMAccountName) """
    conn.search(
        search_base=f"DC={domain_parts[0]},DC={domain_parts[1]}",
        search_filter="(objectClass=user)",
        attributes=["sAMAccountName", "memberOf"]
    )

    return conn.entries

def enumerate_groups(conn: Connection) -> list[str]:
    """ função para enumerar os grupos do Active Directory usando a conexão LDAP estabelecida """

    """ pesquisa por todos os objetos do tipo 'group' no Active Directory e retorna seus nomes de grupo (sAMAccountName) """
    conn.search(
        search_base=f"DC={domain_parts[0]},DC={domain_parts[1]}",
        search_filter="(objectClass=group)",
        attributes=["sAMAccountName", "memberOf"]
    )

    return conn.entries

def enumerate_domain_info(conn: Connection) -> dict:
    """ função para enumerar informações do domínio Active Directory usando a conexão LDAP estabelecida """

    domain_parts = separate_domain()

    """ pesquisa por informações do domínio, como o nome distinto (distinguishedName) e o SID do domínio (objectSid) """
    conn.search(
        search_base=f"DC={domain_parts[0]},DC={domain_parts[1]}",
        search_filter="(objectClass=domain)",
        attributes=["distinguishedName", "objectSid"]
    )

    return conn.entries


