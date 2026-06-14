""" ponto de entrada para a execução do reconhecimento """

from recon.network_scan import scan_network
from recon.port_scan import scan_ports
from recon.service_enum import enumerate_services
from recon.ad_enum import ad_connect, enumerate_users, enumerate_domain_info, enumerate_groups
from core.constants import DC
from exploitation.exploit_windows import WindowsExploit
from exploitation.exploit_web import WebExploit
from exploitation.webScanner import WebScanner
from post_exploitation.index import run_post_exploitation
from reporting.report_builder import gerar_relatorio

def main():
    # 1. Fazer Reconhecimento
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
        print(banners)

    # 2. Enumerar usuários, domínios e grupos do Active Directory usando credenciais de teste
    
    conn = ad_connect(
        "192.168.6.130",
        "PAC\\Administrador",
        "P@ssword123!"
    )

    users = enumerate_users(conn)
    domain_infos = enumerate_domain_info(conn)
    groups = enumerate_groups(conn)

    """
    users = enumerate_users(conn)
        print("\n[+] Usuários do Active Directory encontrados:")
    for user in users:
        print(f"\n{user}")
    
    domain_infos = enumerate_domain_info(conn)
    print("\n[+] Domínios encontrados:")
    for domain_info in domain_infos:
        print(f"\n{domain_info}")

    groups = enumerate_groups(conn)
    print("\n[+] Grupos encontrados:")
    for group in groups:
        print(f"\n{group}")
    """

    target = "192.168.6.129" # Windows 10
    print("\n=== FASE DE EXPLORAÇÃO ===")
    print(f"A iniciar exploração do alvo {target}...")
    
    # 3. Exploração (controlada)
    winexp = WindowsExploit(target)

    exploitation_results = []
    exploitation_results.append(winexp.run_windows_exploit())
    
    # Exemplo: DVWA na máquina alvo
    #web = WebScanner("http://192.168.6.128")

    #print("\n=== FASE DE EXPLORAÇÃO WEB (PYTHON) ===")
    #web.get_title()
    #web.get_headers()
    #web.scan_paths()
    
    #print(exploitation_results)

    # 4. PÓS-EXPLORAÇÃO
    post_results = run_post_exploitation()
    #print("\n=== RESULTADOS DA PÓS-EXPLORAÇÃO ===")
    #print(post_results)

    # 5. Relatório
    gerar_relatorio(hosts, users, domain_infos, groups, exploitation_results, post_results)
    


if __name__ == "__main__":
    main()
    