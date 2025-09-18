import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Substituir pelo canal da sua turma
CHANNEL_ID = "2943258"
URL = f"https://thingspeak.mathworks.com/channels/{CHANNEL_ID}/feeds.json"  # API URL

# Requisição à API
response = requests.get(URL)

# Check for successful response
if response.status_code == 200:
    try:
        data = response.json()

        # Extrair campos
        feeds = data["feeds"]
        umidade = [float(f["field1"]) for f in feeds if f["field1"]]
        temperatura = [float(f["field2"]) for f in feeds if f["field2"]]

        # Converter timestamps para datetime e extrair apenas hora:minuto
        timestamps = [
            datetime.strptime(f["created_at"], "%Y-%m-%dT%H:%M:%SZ").strftime("%H:%M")
            for f in feeds
        ]

        # Gráfico de Umidade
        plt.figure(figsize=(10, 5))
        plt.plot(timestamps, umidade, marker="o", label="Umidade")
        plt.xticks(rotation=45)
        plt.xlabel("Hora")
        plt.ylabel("Umidade")
        plt.legend()
        plt.title("Variação da Umidade")
        plt.tight_layout()
        plt.show()

        # Gráfico de Temperatura
        plt.figure(figsize=(10, 5))
        plt.plot(timestamps, temperatura, marker="o", color="r", label="Temperatura (°C)")
        plt.xticks(rotation=45)
        plt.xlabel("Hora")
        plt.ylabel("Temperatura (°C)")
        plt.legend()
        plt.title("Variação da Temperatura")
        plt.tight_layout()
        plt.show()

    except requests.exceptions.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print("Response content:", response.text)

else:
    print(f"Error: API request failed with status code {response.status_code}")
    print("Response content:", response.text)
