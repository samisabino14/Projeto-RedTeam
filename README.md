# Projeto Red Team Automatizado
Projeto de Programação Aplicada à Cibersegurança II do IIº semestre do 1º ano de CTeSP no Instituto Politécnico de Setúbal


## Descrição do Projeto

Este projeto implementa um pipeline académico de Red Teaming totalmente automatizado, desenvolvido em Python e integrado com o Metasploit Framework através da interface RPC (MSGRPC).  
O objetivo é demonstrar, num ambiente controlado, as fases essenciais de um ataque estruturado:

- Reconhecimento  
- Enumeração  
- Exploração  
- Pós‑Exploração  
- Análise e relatório  

Todo o processo é executado sobre máquinas virtuais isoladas, garantindo segurança e controlo total do ambiente.  
O script principal (`main.py`) coordena todas as fases, comunicando com o Metasploit via RPC e recolhendo resultados para análise.

---

## Ambiente de Laboratório

O projeto foi desenvolvido num ambiente virtualizado composto por:

- **Máquina Atacante**
  - Kali Linux
  - Metasploit Framework
  - PostgreSQL
  - Python 3 + venv
  - Scripts de automação (VScode)

- **Máquina Alvo**
  - Windows 10
  - Configuração padrão de rede
  - Serviços expostos (RDP, SMB, HTTP)
  - Ambiente isolado e seguro

- **Máquina Controladora de Domínio**
    - Windows Server
    - Active Directory
    - LDAP habilitado
    - Utilizadores configurados para testes

Este ambiente permite simular cenários reais de ataque sem risco para sistemas externos.

---

## Requisitos

Antes de executar o projeto, certifique‑se de que possui:

- Python 3.13
- Ambiente virtual (venv)
- Metasploit Framework instalado
- PostgreSQL ativo
- Acesso ao módulo `msgrpc`
- Git (opcional, para versionamento)

---

## Como Utilizar o Projeto:

---

### **1. Preparar o ambiente (Configurar as Máquinas)**
    - Utilize o relatório para ver o que é necessário para preparar o ambiente.

### **2. Colocar todas as máquinas na mesma rede Host-Only**

### **3. Criar Snapshots**

### **4. Rodar Metasploit RPC (no terminal)**

- Iniciar o serviço: (PostgreSQL): 
```bash
sudo systemctl start PostgreSQL
- Inicializar a BD de Metasploit Interface: 
```bash
sudo msfdb init
- Entrar na console de Metasploit Interface: 
```bash
msfconsole
- Dentro da msfconsole: load msgrpc Pass="r368Duzz"

Nota: O Metasploit utiliza PostgreSQL como backend.  

### **5. Rodar o main.py**
Ativar o Ambiente Virtual (venv):
```bash
source venv/bin/activate

```bash
python3 main.py

Nota: deve ser rodado dentro do venv na pasta do projeto

