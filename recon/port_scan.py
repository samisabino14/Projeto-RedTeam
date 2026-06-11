""" varredura de portas """
import socket
from core.constants import COMMON_PORTS

def scan_ports(ip: str, ports: list[int] = COMMON_PORTS) -> list[int]:
    """ função de varredura de portas para identificar serviços ativos em um host """
    
    """ lista para armazenar portas abertas encontradas no host """
    open_ports = {}
    
    """ itera sobre as portas fornecidas e verifica quais estão abertas usando sockets """
    for port in ports:

        """ cria um socket TCP para tentar se conectar à porta no host """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Define um timeout de 0.5 segundo para a conexão

        try:
            """ tenta conectar à porta no host e verifica se a conexão foi bem-sucedida """
            result = sock.connect_ex((ip, port))
            
            is_open = (result == 0)
            
            """ armazena o status da porta (aberta ou fechada) no dicionário de portas abertas """
            open_ports[port] = is_open
            
            status = "ABERTA" if is_open else "fechada"

            print(f"[SCANNING] Porta {port} está {status} no host {ip}")
 
        except Exception as e:
            print(f"Erro ao verificar a porta {port} no host {ip}: {e}")
            open_ports[port] = False
        finally:
            sock.close()

    return open_ports