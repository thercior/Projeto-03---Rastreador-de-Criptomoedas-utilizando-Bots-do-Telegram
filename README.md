# Projeto-03---Rastreador-de-Criptomoedas-utilizando-Bots-do-Telegram
<!-- Emoji e Language Tools -->
<div style="display: inline_block"><br>
 <img align="center" alt="Thercio-Python" height="50" width="60" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
</div>

## **Descrição**

<div class = "text-justify">

Projeto de um bot telegram para rastreamento de criptomoedas, desenvolvido para praticar os conhecimentos e habilidades adquiridos  junto ao curso Jornada Python da Python Academy, utilizando a linguagem Python.

</div>

## **Pré requisitos**
<div class = "text-justify">

As bibliotecas utilizadas que se encontram no arquivo [requirements.txt](https://github.com/thercior/Projeto-03---Rastreador-de-Criptomoedas-utilizando-Bots-do-Telegram/blob/main/requirements.txt) foram:

</div>
  
  - *python-telegram-bot para criação do Bot e envio de mensagens.*
  - *request para fazer requisição de API.*

Deve-se também criar um bot do telegram. [Crie seu bot Telegram clicando aqui e seguindo estas instruções](https://canaltech.com.br/apps/como-criar-um-bot-no-telegram-botfather/)

Após criar o bot, criar um token de acesso, e gravar em um arquivo token.txt que deve ficar na raiz do projeto. Este arquivo contendo o token do bot é necessário para o programa ter acesso ao bot do telegram criado.

  **OBSERVAÇÃO: Não compartilhe seu token com ninguém. É ele quem dá acesso e controle ao seu bot.**


<div class = "text-justify">

A Biblioteca python-telegram-bot teve que ser especificada no requeriments.txt em uma versão específica, a 13.11, devido a problemas de dependências.

</div>

## **API utilizada**
Para consulta e obtenção das cotações de criptomoedas foi utilizado a [API da Coingecko](https://www.coingecko.com/pt/api/documentation).
  
## **Composição e execução**

<div class = "text-justify">

O programa é composto de dois arquivos: [Projeto](https://github.com/thercior/Projeto-03---Rastreador-de-Criptomoedas-utilizando-Bots-do-Telegram/blob/main/project-rastreador.py) e [Models](https://github.com/thercior/Projeto-03---Rastreador-de-Criptomoedas-utilizando-Bots-do-Telegram/blob/main/models.py).

O Models é para criação e instanciação de Classes/Objetos e Métodos.

O Projeto é o programa principal, que executa e roda a aplicação. Para rodar, basta executar no terminal:
  **python project-rastreador.py

Após a execução, será pedido para informar

 - *Id da criptomoeda*
 - *Valor mínimo de cotação para iniciar o rastreamento*
 - *Valor máximo de cotação para iniciar o rastreamento*

Após informar, o programa começará a rodar e informará o valor da cotação da criptomoeda escolhida sempre o que os critérios forem obedecido.
Para envio de cotações recorrente, deve-se importar o método Sleep da biblioteca time e definir um tempo de espera entre uma consulta e outra. Defina sleep(x), onde x é o tempo em segundos que você deseja entre uma consulta e outra.

</div>
