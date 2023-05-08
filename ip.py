import requests

# Faz uma requisição GET ao site ipify
response = requests.get('https://api.ipify.org')

# Obtém o endereço de IP da resposta
ip = response.text

print(f"Seu endereço de IP é: {ip}")

# Explicacação linha por linha:

# import requests: Importa a biblioteca requests para permitir que o código faça solicitações HTTP para a API.
                    # HTTP: protocolo de comunicação utilizado para transferência de dados na Web.

# response = requests.get('https://api.ipify.org'): Faz uma solicitação HTTP GET para a API do ipify.org usando a função get() da biblioteca requests. A resposta é armazenada na variável response.
                    # GET: utilizado para solicitar dados de um recurso específico da API

# ip = response.text: Extrai o endereço IP da resposta da API, que é retornada no formato de texto, e armazena-o na variável ip

# print(f"Seu endereço de IP é: {ip}"): Imprime uma mensagem ao usuário que inclui o endereço IP retornado pela API. 
                    # o f antes de uma string indica que ela é uma f-string (format string)
                    # a f-string é uma forma de incorporar o valor de uma variável em uma string, sem precisar usar concatenação ou formatação complexa.








