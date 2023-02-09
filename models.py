import requests
import telegram

class ApiCripto:
    def __init__(self, url_base: str):
        self.url_base = url_base
    
    def ping(self) -> bool:
        print('Verificando se API está online')
        url = f'{self.url_base}/ping'
        return requests.get(url).status_code == 200
    
    def consulta_cripto(self, id_moeda: str):
        print(f'Consultando o preçop da moeda de ID = {id_moeda}...')
        url = f'{self.url_base}/simple/price?ids={id_moeda}&vs_currencies=BRL&include_last_updated_at=true'
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            dados_moeda = resposta.json().get(id_moeda, None)
            preco = dados_moeda.get('brl',None)
            atualizado_em = dados_moeda.get('last_updated_at',None)
            return preco, atualizado_em
            
        else:
            raise ValueError(f'Código de resposta diferente de HTTP 200 ok {resposta.status_code}')


class TelegramBot:
    def __init__(self, token: str, chat_id: int) -> None:
        self.bot = telegram.Bot(token=token)
        self.token = token
        self.chat_id = chat_id
        
    def enviar_msg(self, texto_markdown):
        self.bot.send_message(
            text = texto_markdown, 
            chat_id=self.chat_id,
            parse_mode=telegram.ParseMode.MARKDOWN
        )
        print('Mensagem enviada com sucesso!')