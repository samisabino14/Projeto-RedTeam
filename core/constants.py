""" constantes globais """

COMMON_PORTS = [
    21, 
    22, 
    25, 
    53, 
    80, 
    110, 
    143,
    389, 
    443, 
    445,
    3306, 
    3389, 
    5900,
    5985,
    5985,
    8080, 
    8443
]

PORT_SERVICES = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5985: "WinRM",
}

DC = {
    "domain": "pac.local",
    "user": "administrator",
    "password": "P@ssword123!"
}

IPs = {
    "local_network": {
        "ip": "192.168.6.128",
        "cidr": "192.168.6.128/24"
    }
}