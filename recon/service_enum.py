""" enumeração de serviços """
import socket, ssl
from core.constants import PORT_SERVICES

def grab_banner(ip: str, port: int) -> str:
    """ Captura o banner de um serviço ou identifica o protocolo mesmo sem banner """
    try:
        sock = socket.socket()
        sock.settimeout(1)

        # -------------------------
        # HTTPS (porta 443)
        # -------------------------
        if port == 443:
            context = ssl.create_default_context()
            conn = context.wrap_socket(sock, server_hostname=ip)
            conn.connect((ip, port))
            conn.send(b"HEAD / HTTP/1.0\r\n\r\n")
            data = conn.recv(1024)
            return data.decode(errors='ignore') or "HTTPS detectado (sem banner)"

        # -------------------------
        # HTTP (porta 80, 8080, 8443)
        # -------------------------
        if port in [80, 8080, 8443]:
            sock.connect((ip, port))
            sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
            data = sock.recv(1024)
            return data.decode(errors='ignore') or "HTTP detectado (sem banner)"

        # -------------------------
        # Protocolos que NÃO têm banner
        # -------------------------
        if port in [53, 389, 445, 3389]:
            service = PORT_SERVICES.get(port, "Serviço desconhecido")
            return f"{service} detectado (sem banner)"

        # -------------------------
        # Protocolos com banner em texto (FTP, SSH, SMTP, POP3, IMAP)
        # -------------------------
        sock.connect((ip, port))
        data = sock.recv(1024)

        if data:
            return data.decode(errors='ignore')

        return f"{PORT_SERVICES.get(port, 'Serviço desconhecido')} detectado (sem banner)"

    except Exception as e:
        return "Banner não disponível"

    finally:
        try:
            sock.close()
        except:
            pass


def enumerate_services(ip: str, open_ports: list[int]) -> dict[int, str]:
    """ função para enumerar os serviços ativos em um host com base nas portas abertas """
    
    """ dicionário para armazenar os banners dos serviços encontrados nas portas abertas """
    service_banners = {}
    
    """ itera sobre as portas abertas e captura o banner de cada serviço usando a função grab_banner """
    for port in open_ports:
        print(f"[ENUMERAÇÃO] A capturar banner do serviço na porta {port} do host {ip}...")
        banner = grab_banner(ip, port)

        """ armazena o banner do serviço no dicionário de banners de serviços """
        service_banners[port] = banner.strip() if banner else "Banner não disponível"
    
    return service_banners

