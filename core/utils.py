""" funções auxiliares """
from core.constants import DC

def separate_domain():
    """ pegar o domínio em partes e imprimir cada parte separadamente """
    domain_parts = DC["domain"].split(".")
    
    return domain_parts