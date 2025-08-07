### Universidade Estadual do Oeste do Paraná
### Disciplina: Redes de Computadores

---

#### **Trabalho proposto:**
- Implementar um cliente e um servidor.
- Realizar trocas de mensagens entre eles com diferentes parametros (tamanho de mesagem e número de repetições).
- Detalhes podem ser vistos no PDF [Trabalho Redes 2025 - Desempenho TCP e UDP](https://github.com/yVinicin/Comparacao-de-Desempenho-TCP-e-UDP/blob/main/Trabalho%20Redes%202025%20-%20Desempenho%20TCP%20e%20UDP.pdf).

---

### Execução (Linux):
- Servidor (TCP)
```
pyhton3 servidor.py tcp <msg> <tam_msg> <num_repeticoes>
```

- Servidor (UDP)
```
pyhton3 servidor.py udp <msg> <tam_msg> <num_repeticoes>
```

- Cliente (TCP)
```
pyhton3 cliente.py tcp <msg> <tam_msg> <num_repeticoes>
```

- Cliente (UDP)
```
pyhton3 cliente.py udp <msg> <tam_msg> <num_repeticoes>
```

---

### Execução (Windows):
- Servidor (TCP)
```
pyhton servidor.py tcp <msg> <tam_msg> <num_repeticoes>
```

- Servidor (UDP)
```
pyhton servidor.py udp <msg> <tam_msg> <num_repeticoes>
```

- Cliente (TCP)
```
pyhton cliente.py tcp <msg> <tam_msg> <num_repeticoes>
```

- Cliente (UDP)
```
pyhton cliente.py udp <msg> <tam_msg> <num_repeticoes>
```
