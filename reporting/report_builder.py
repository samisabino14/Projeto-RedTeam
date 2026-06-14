""" construtor de relatórios para apresentação dos resultados da exploração e pós-exploração """
def gerar_relatorio(hosts, users, domain_info, groups, exploitation_results, post_results):
    print("\n========== RELATÓRIO FINAL ==========\n")

    print("=== Hosts Identificados ===")
    for host in hosts:
        print(host)

    print("\n=== Utilizadores AD ===")
    for user in users:
        print(user)

    print("\n=== Informações do Domínio ===")
    print(domain_info)

    print("\n=== Grupos encontrados: ===")
    for group in groups:
        print(f"\n{group}")

    print("\n=== Resultados da Exploração ===")
    for result in exploitation_results:
        print(result)

    print("\n=== Pós-Exploração ===")
    print(post_results)

    print("\n=====================================\n")
