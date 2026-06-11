""" varredura de rede """
import ipaddress, subprocess

def ping_host(ip: str) -> bool:
    """ função de ping para verificar se o host está ativo """
    
    try:
        # Executa o comando ping (4 pacotes, timeout de 1 segundo)
        result = subprocess.run(
            ["ping", "-c", "4", "-W", "1", ip],
            stdout=subprocess.DEVNULL,  # Ignora a saída do comando
            stderr=subprocess.DEVNULL,  # Ignora a saída de erro do comando
        )
        
        return result.returncode == 0  # Retorna True se o ping foi bem-sucedido
    except Exception as e:
        print(f"Erro ao pingar o host {ip}: {e}")
        return False
    
def scan_network(cidr: str):
    """ função de varredura de rede para identificar hosts ativos """
    
    """ cria um objeto de rede a partir do CIDR fornecido """
    network = ipaddress.ip_network(cidr, strict=False)
    
    """ lista para armazenar hosts ativos encontrados na rede """
    active_hosts = []

    """ itera sobre os hosts na rede e verifica quais estão ativos usando a função de ping """
    for ip in network.hosts():
        ip_str = str(ip)
        
        print(f"[RECONHECIMENTO] A verificar host: {ip_str}")

        if ping_host(ip_str):
            print(f"[RECONHECIMENTO] Host ativo encontrado: {ip_str}")
            active_hosts.append(ip_str)

    return active_hosts


