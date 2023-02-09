from datetime import datetime
from models import ApiCripto, TelegramBot
import locale
from time import sleep

id_moeda = input('Qual o ID da moeda ser rastreada?\n \t')
valor_min = int(input('Qual o valor mínimo para iniciar o rastreamento? \n \t'))
valor_max = int(input('Qual o valor máximo para iniciar o rastreamento? \n \t'))
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#Instanciando a classe da api e do bot
    #Lembrar de criar o arquivo token.txt inserido a chave token exclusiva do seu bot
token = open('./token.txt').readline() #ler o token no arquivo token.
id = open('./chat_id.txt').readline() #ler o id da conversa com o bot
api = ApiCripto(url_base='https://api.coingecko.com/api/v3') # api de consulta da cripto moeda
bot = TelegramBot(token=token, chat_id=id) # envia os parâmetros do bot para instância das classes criadas

# Rastreamento de cotação de criptmoeda e retorno para o bot do Telegram criado
while True:
    
    if api.ping():
        print('API Online')
        preco, atualizado_em = api.consulta_cripto(id_moeda=id_moeda)
        print('Consulta realizada com Sucesso!')
        data_hora = datetime.fromtimestamp(atualizado_em).strftime('%x %X')
        mensagem = None
        
        if preco < valor_min:
            mensagem = f'*A cotação do Ethereum é de:* \n \t *Preço:* R$ {preco:.2f} \n \t *Atualizado em:* {data_hora}' \
                f'\n \t Motivo: valor menor que o mínimo'
        
        if preco > valor_max:
            mensagem = f'*A cotação do Ethereum é de:* \n \t *Preço:* R$ {preco} \n \t *Atualizado em:* {data_hora}' \
                f'\n \t *Motivo*: valor maior que o máximo'
        
        if mensagem:
            bot.enviar_msg(texto_markdown=mensagem)
    else:
        print('API Offline. Tente novamente mais tarde')
    
    sleep(5)