# 📡 Comparação de Desempenho TCP vs UDP

> Análise prática e comparativa de desempenho entre os protocolos de transporte TCP e UDP, desenvolvida para a disciplina de Redes de Computadores.

![Badge Python](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white)
![Badge Network](https://img.shields.io/badge/Topic-Computer%20Networks-blue?logo=cisco&logoColor=white)
![Badge Academic](https://img.shields.io/badge/Type-Academic%20Project-orange)

## 🏫 Sobre o Projeto

Este projeto foi desenvolvido como parte da avaliação da disciplina de **Redes de Computadores** da **Universidade Estadual do Oeste do Paraná (Unioeste)**.

O objetivo é implementar uma aplicação cliente-servidor capaz de transmitir dados via **TCP** (orientado a conexão) e **UDP** (não orientado a conexão), permitindo a medição e comparação de métricas como tempo de envio, latência e confiabilidade em diferentes cenários (Localhost, Cabo-Cabo, Wi-Fi).

## 📂 Estrutura do Projeto

```bash
Comparacao-de-Desempenho-TCP-e-UDP/
├── servidor.py    # Script que recebe as requisições (TCP/UDP)
├── cliente.py     # Script que envia os dados e mede o tempo
├── protocolos.py  # Definições comuns e utilitários
├── Relatório...   # Análise detalhada dos testes realizados
└── Testes_...txt  # Logs com os resultados obtidos nos cenários
```

## 🚀 Como Executar

Certifique-se de ter o **Python 3** instalado. A execução requer que o **servidor** seja iniciado antes do **cliente**.

### Sintaxe Geral
Os scripts esperam argumentos na seguinte ordem:
`python arquivo.py <protocolo> <mensagem> <tamanho_bytes> <repeticoes>`

### Passo a passo

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/yVinicin/Comparacao-de-Desempenho-TCP-e-UDP.git
    cd Comparacao-de-Desempenho-TCP-e-UDP
    ```

2.  **Inicie o Servidor:**
    Escolha o protocolo (tcp ou udp) e defina os parâmetros.
    * **Linux/Mac:**
      ```bash
      python3 servidor.py tcp "Teste" 1024 100
      ```
    * **Windows:**
      ```bash
      python servidor.py tcp "Teste" 1024 100
      ```

3.  **Inicie o Cliente:**
    Em outro terminal, execute o cliente com os mesmos parâmetros para iniciar a transmissão.
    * **Linux/Mac:**
      ```bash
      python3 cliente.py tcp "Teste" 1024 100
      ```
    * **Windows:**
      ```bash
      python cliente.py tcp "Teste" 1024 100
      ```

## 📊 Cenários de Teste

Os arquivos `.txt` no repositório contêm resultados de testes realizados em diferentes meios físicos:
* **Localhost:** Comunicação interna na mesma máquina.
* **Cabo-Cabo:** Dois computadores conectados via Ethernet.
* **Wi-Fi:** Comunicação via rede sem fio.
