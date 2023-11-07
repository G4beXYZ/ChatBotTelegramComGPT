# Telegram ChatBot template

Esse bot é um assistente interativo do Telegram que fornece informações sobre a Estação Espacial Internacional (ISS), gera memes aleatórios, compartilha imagens de cachorros fofos, e muito mais. Ele é projetado para entreter e educar os usuários sobre o espaço e oferecer leveza com conteúdo divertido.

## Funcionalidades

- `/start`: Sauda o usuário com uma mensagem de boas-vindas personalizada.
- `/iss`: Informa a localização atual da ISS, o número de pessoas a bordo e a hora UTC atual.
- `/meme`: Envia um meme aleatório para o usuário.
- `/doggo`: Compartilha uma imagem aleatória de cachorro.

## Tecnologias Utilizadas

- Python 3.8+
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) (TeleBot)
- APIs externas:
  - Open Notify API para informações da ISS.
  - Imgflip API para memes.
  - RandomDog API para imagens de cachorros.

## Instalação e Configuração

Para rodar este bot, siga os passos abaixo:

1. Clone o repositório para a sua máquina local usando:
   ```bash
   git clone https://github.com/G4beXYZ/ChatBotTelegramComGPT
   ```

Navegue até o diretório do projeto:
 ```bash
  cd seu-bot-telegram
  ```
pip install -r requirements.txt
Crie um arquivo .env na raiz do projeto com as seguintes variáveis de ambiente baseadas no arquivo .env.example.
Inicie o bot com:
bash
Copy code
python main.py
Variáveis de Ambiente
As seguintes variáveis de ambiente são necessárias para o funcionamento do bot:

TELEBOT_TOKEN: O token de autenticação fornecido pelo BotFather do Telegram.
OPENAI_TOKEN: (Opcional) A chave de API para o OpenAI, se recursos adicionais baseados em GPT forem utilizados.
LOT_API_KEY: (Opcional) A chave de API para 'The One API' para recursos relacionados ao Senhor dos Anéis.
Exemplo de .env:

makefile
Copy code
TELEBOT_TOKEN=your_telegram_bot_token_here
OPENAI_TOKEN=your_openai_api_key_here
LOT_API_KEY=your_lord_of_the_rings_api_key_here
Contribuição
Contribuições são bem-vindas! Se você tiver uma sugestão de melhoria, sinta-se à vontade para fazer um fork do repositório e enviar um pull request, ou abrir um issue com a tag "melhoria".

Licença
Este projeto é licenciado sob a Licença MIT - veja o arquivo LICENSE.md para detalhes.

Contato
Para entrar em contato, por favor, envie um e-mail para seuemail@dominio.com.
