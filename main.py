""" ponto de entrada para a execução do reconhecimento """

from recon.network_scan import scan_network
from recon.port_scan import scan_ports
from recon.service_enum import enumerate_services
from recon.ad_enum import ad_connect, enumerate_users, enumerate_domain_info
from core.constants import DC, IPs
from exploitation.msf_rpc import MetasploitRPC

def main():
    print("\n[+] A iniciar o Reconhecimento...")
    #hosts = scan_network(IPs["local_network"]["cidr"])
    hosts = ["192.168.6.128", "192.168.6.129", "192.168.6.130",]
    
    print("\n[+] A fazer port scan nos hosts ativos...")
    for host in hosts:
        print(f"\n[+] Scanning host: {host}")
        ports = scan_ports(host)
        
        """ filtra as portas abertas a partir dos resultados do port scan """
        open_ports = [port for port, status in ports.items() if status]

        """ se houver portas abertas, realiza a enumeração de serviços para identificar os serviços em execução e suas versões """
        banners = enumerate_services(host, open_ports)
    
    # Enumerar usuários do Active Directory usando credenciais de teste

    #conn = ad_connect(
    #    "192.168.6.130",
    #    "PAC\\Administrador",
    #    "P@ssword123!"
    #)

    #users = enumerate_users(conn)
    #domain_infos = enumerate_domain_info(conn)

    #print("\n[+] Usuários do Active Directory encontrados:")
    #for user in users:
    #    print(f"\n\n{user}")
def main2():
    MetasploitRPC()   

if __name__ == "__main__":
    main2()
    