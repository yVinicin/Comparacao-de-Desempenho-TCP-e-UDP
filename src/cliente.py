#!/usr/bin/env python3
import sys
from protocolos import *

def main():
    if len(sys.argv) != 5:
        print("Uso: ./testar tcp|udp <msg> <tam_msg> <num_repeticoes>")
        sys.exit(1)

    protocolo = str(sys.argv[1])
    msg = sys.argv[2]
    tam_msg = int(sys.argv[3])
    repeticoes = int(sys.argv[4])

    # Alterar conforme o necessário
    ip_addr = '192.168.0.100'
    port = 8000

    if protocolo == "tcp":
        protocolo_tcp = TCP(ip_addr, port, msg, tam_msg, repeticoes)
        protocolo_tcp.cliente()
    elif protocolo == "udp":
        protocolo_udp = UDP(ip_addr, port, msg, tam_msg, repeticoes)
        protocolo_udp.cliente()
    else:
        print("Erro: protocolo inválido, utilize TCP ou UDP")
        sys.exit(1)

if __name__ == "__main__":
    main()
