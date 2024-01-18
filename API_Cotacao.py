import requests
import json
a = "https://economia.awesomeapi.com.br/json/last/:moedas"
x = int(input("Tecle o digito para a moeda desejada: \n 1 - $USD\n 2 - € EURO\n\n"))
if x == 1:
    dolar = a.replace(':moedas', 'USD-BRL')
    cotacao = requests.get(dolar)
    cotacao = cotacao.json()
    print(f"A cotação atual do dolar está : R$ {cotacao["USDBRL"]["bid"]}")
elif x == 2:
    reais = a.replace(':moedas', 'EUR-BRL')
    cotacao = requests.get(reais)
    cotacao = cotacao.json()
    print(f"A cotação atual do euro está : R$ {cotacao["EURBRL"]["bid"]}")








