# 🌡️ Dashboard IoT com ThingSpeak (Python)

Este projeto tem como objetivo explorar a **API HTTP do ThingSpeak** para leitura de dados de sensores e visualização em gráficos.  
No exemplo, utilizamos dois campos de um canal:  

- **Field 1:** Umidade  
- **Field 2:** Temperatura  

Os dados são coletados diretamente da API do ThingSpeak e plotados em gráficos de linha com **Matplotlib**.

---

## 🚀 Tecnologias Utilizadas
- [Python 3](https://www.python.org/)
- [Requests](https://pypi.org/project/requests/) → para consumir a API HTTP do ThingSpeak  
- [Matplotlib](https://matplotlib.org/) → para gerar os gráficos  
- [Datetime](https://docs.python.org/3/library/datetime.html) → para manipulação de datas  

---

## 📡 Fonte dos Dados
Os dados são extraídos de um canal do **ThingSpeak**, definido pela variável:

```python
CHANNEL_ID = "2943258"
URL = f"https://thingspeak.mathworks.com/channels/{CHANNEL_ID}/feeds.json"
⚠️ Se o canal exigir API Key, basta acrescentar ?api_key=SUA_KEY ao final da URL.

📊 Funcionalidades
Consome dados de umidade e temperatura de um canal IoT.

Converte os timestamps para o formato HH:MM.

Gera dois gráficos interativos:

Variação da Umidade

Variação da Temperatura

🖼️ Exemplo de Dashboard
Gráfico de Umidade
Exibe a evolução da umidade ao longo do tempo.

Gráfico de Temperatura
Mostra a variação da temperatura em °C no mesmo período.

⚙️ Como Executar
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/thingspeak-dashboard.git
cd thingspeak-dashboard
Instale as dependências:

bash
Copiar código
pip install requests matplotlib
Execute o script:

bash
Copiar código
python main.py
Os gráficos serão exibidos em janelas interativas.

📌 Estrutura do Projeto
bash
Copiar código
📂 thingspeak-dashboard
 ├── main.py        # Código principal
 ├── README.md      # Documentação
 └── requirements.txt (opcional)
Se quiser, você pode gerar o requirements.txt com:

bash
Copiar código
pip freeze > requirements.txt
👨‍💻 Autor
Projeto desenvolvido para a disciplina Arquitetura e Protocolos IoT, explorando a integração com o ThingSpeak.

