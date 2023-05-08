import requests

# Faz uma requisição GET ao site ipify
response = requests.get('https://api.ipify.org')

# Obtém o endereço de IP da resposta
ip = response.text

print(f"Seu endereço de IP é: {ip}")

