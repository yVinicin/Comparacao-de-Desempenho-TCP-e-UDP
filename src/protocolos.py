import socket
import time

class TCP:
    def __init__(self, ip, porta, msg, tam_msg, num_repeticoes):
        self.ip = ip
        self.porta = porta
        self.msg = msg
        self.tam_msg = tam_msg
        self.num_repeticoes = num_repeticoes

    def servidor(self):
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        servidor.bind((self.ip, self.porta))
        servidor.listen(0)
        print(f"Aguardando... {self.ip}:{self.porta}")
        cliente_socket, cliente_addr = servidor.accept()
        print(f"Conectado com {cliente_addr[0]}:{cliente_addr[1]}")

        for _ in range(self.num_repeticoes):
            request = cliente_socket.recv(self.tam_msg) # tamanho do buffer
            if not request:
                break

            self.msg = request.decode()
            print(f"Menssagem recebida: {self.msg}")

            resposta = "Recebida!"
            cliente_socket.send(resposta.encode())

        cliente_socket.close()
        servidor.close()

    def cliente(self):
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((self.ip, self.porta))

        total_bytes_enviados = 0
        mensagens_enviadas = 0
        mensagens_recebidas = 0

        inicio = time.time()

        for _ in range(self.num_repeticoes):
            cliente.send(self.msg.encode())
            total_bytes_enviados += len(self.msg)
            mensagens_enviadas += 1

            try:
                resposta = cliente.recv(self.tam_msg)
                if resposta:
                    mensagens_recebidas += 1
            except:
                pass

        fim = time.time()
        duracao = fim - inicio
        throughput = total_bytes_enviados / duracao if duracao > 0 else 0
        perdas = mensagens_enviadas - mensagens_recebidas

        print("\n--- MEDIÇÕES TCP ---")
        print(f"Tempo total de envio: {duracao:.4f} segundos")
        print(f"Throughput: {throughput:.2f} bytes/segundo")
        print(f"Mensagens enviadas: {mensagens_enviadas}")
        print(f"Mensagens recebidas: {mensagens_recebidas}")
        print(f"Mensagens perdidas: {perdas}")

        cliente.close()


class UDP:
    def __init__(self, ip, porta, msg, tam_msg, num_repeticoes):
        self.ip = ip
        self.porta = porta
        self.msg = msg
        self.tam_msg = tam_msg
        self.num_repeticoes = num_repeticoes

    def servidor(self):
        udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        server_address = (self.ip, self.porta)

        udp_server_socket.bind(server_address)

        print("Servidor UDP aguardando mensagens...")

        for _ in range(self.num_repeticoes):
            data, self.address = udp_server_socket.recvfrom(self.tam_msg)
            print(f"Mensagem recebida: {data.decode()} de {self.address}")

            response = "Mensagem recebida com sucesso"
            udp_server_socket.sendto(response.encode(), self.address)
            print(f"Resposta enviada para {self.address}")


    def cliente(self):
        udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = (self.ip, self.porta)
        udp_client_socket.settimeout(1.0)

        total_bytes_enviados = 0
        mensagens_enviadas = 0
        mensagens_recebidas = 0

        inicio = time.time()

        for _ in range(self.num_repeticoes):
            udp_client_socket.sendto(self.msg.encode(), server_address)
            total_bytes_enviados += len(self.msg)
            mensagens_enviadas += 1

            try:
                data, _ = udp_client_socket.recvfrom(self.tam_msg)
                if data:
                    mensagens_recebidas += 1
            except socket.timeout:
                pass  # timeout é considerado perda

        fim = time.time()
        duracao = fim - inicio
        throughput = total_bytes_enviados / duracao if duracao > 0 else 0
        perdas = mensagens_enviadas - mensagens_recebidas

        print("\n--- MEDIÇÕES UDP ---")
        print(f"Tempo total de envio: {duracao:.4f} segundos")
        print(f"Throughput: {throughput:.2f} bytes/segundo")
        print(f"Mensagens enviadas: {mensagens_enviadas}")
        print(f"Mensagens recebidas: {mensagens_recebidas}")
        print(f"Mensagens perdidas: {perdas}")

        udp_client_socket.close()
