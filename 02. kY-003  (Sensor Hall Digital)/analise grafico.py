import matplotlib.pyplot as plt

# Função para ler os dados do arquivo
def ler_dados(arquivo):
    tempos = []
    valores_hall = []
    valores_buzzer = []
    
    with open(arquivo, 'r') as f:
        for linha in f:
            if linha.strip():  # Ignora linhas em branco
                tempo, hall, buzzer = linha.split()
                tempos.append(float(tempo))
                valores_hall.append(int(hall))
                valores_buzzer.append(int(buzzer))
    
    return tempos, valores_hall, valores_buzzer

# Ler os dados do arquivo
arquivo_dados = "dados_sensor2.txt"
tempos, valores_hall, valores_buzzer = ler_dados(arquivo_dados)

# Plotar os dados
plt.figure(figsize=(12, 6))

# Gráfico do Sensor Hall
plt.subplot(2, 1, 1)
plt.plot(tempos, valores_hall, label='Sensor Hall', color='blue')
plt.xlabel('Tempo (s)')
plt.ylabel('Sensor Hall (0/1)')
plt.title('Leitura do Sensor Hall ao longo do tempo')
plt.grid(True)
plt.legend()

# Gráfico do Buzzer
plt.subplot(2, 1, 2)
plt.plot(tempos, valores_buzzer, label='Buzzer', color='red')
plt.xlabel('Tempo (s)')
plt.ylabel('Buzzer (0/1)')
plt.title('Estado do Buzzer ao longo do tempo')
plt.grid(True)
plt.legend()

# Ajusta o layout dos gráficos
plt.tight_layout()

# Mostrar os gráficos
plt.show()
