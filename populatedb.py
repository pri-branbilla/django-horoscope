import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'horoscopo.settings')

import django
django.setup()

import random
from hsite.models import Signos

signos = [
    {
        'nome': 'Áries',
        'data': '21/03 - 20/04',
        'img': 'https://conteudo.imguol.com.br/c/entretenimento/6a/2018/02/28/signo-aries-1519860677782_v2_300x225.jpg',
        'nomelink': 'aries',
    },
    {
        'nome': 'Touro',
        'data': '21/04 - 20/05',
        'img': 'https://conteudo.imguol.com.br/c/entretenimento/15/2018/02/28/signo-touro-1519861435391_v2_300x225.jpg',
        'nomelink': 'touro',
    },
    {
        'nome': 'Gêmeos',
        'data': '21/05 - 20/06',
        'img': 'https://conteudo.imguol.com.br/c/entretenimento/bb/2018/02/28/signo-gemeos-1519861127123_v2_300x225.jpg',
        'nomelink': 'gemeos',
    },
    {
        'nome': 'Câncer',
        'data': '21/06 - 21/07',
        'img': 'https://conteudo.imguol.com.br/c/entretenimento/ff/2018/02/28/signo-1519860763866_v2_300x225.jpg',
        'nomelink': 'cancer',
    },
    {
        'nome': 'Leão',
        'data': '22/07 - 22/08',
        'img': 'https://conteudo.imguol.com.br/c/entretenimento/68/2018/02/28/signo-leao-1519861195963_v2_300x225.jpg',
        'nomelink': 'leao',
    },
    {
        'nome': 'Virgem',
        'data': '23/08 - 22/09',
        'img': 'https://conteudo.imguol.com.br/c/entretenimento/ba/2018/02/28/signo-virgem-1519861496372_v2_300x225.jpg',
        'nomelink': 'virgem',
    },
    {
        'nome': 'Libra',
        'data': '23/09 - 22/10',
        'img': 'https://conteudo.imguol.com.br/c/entretenimento/83/2018/02/28/signo-libra-1519861267568_v2_300x225.jpg',
        'nomelink': 'libra',
    },
    {
        'nome': 'Escorpião',
        'data': '23/10 - 21/11',
        'img': 'https://conteudo.imguol.com.br/c/entretenimento/b4/2018/02/28/signo-escorpiao-1519861039649_v2_300x225.jpg',
        'nomelink': 'escorpiao',
    },
    {
        'nome': 'Sagitário',
        'data': '22/11 - 21/12',
        'img': 'https://conteudo.imguol.com.br/c/entretenimento/2e/2018/02/28/signo-sagitario-1519861378822_v2_300x225.jpg',
        'nomelink': 'sagitario',
    },
    {
        'nome': 'Capricórnio',
        'data': '22/12 - 20/01',
        'img': 'https://conteudo.imguol.com.br/c/entretenimento/0d/2018/02/28/signo-capricornio-1519860896802_v2_300x225.jpg',
        'nomelink': 'capricornio',
    },
    {
        'nome': 'Aquário',
        'data': '21/01 - 19/02',
        'img': 'https://conteudo.imguol.com.br/c/entretenimento/14/2018/02/28/signo-aquario-1519860613780_v2_300x225.jpg',
        'nomelink': 'aquario',
    },
    {
        'nome': 'Peixes',
        'data': '20/02 - 20/03',
        'img': 'https://conteudo.imguol.com.br/c/entretenimento/34/2018/02/28/signo-peixes-1519861322662_v2_300x225.jpg',
        'nomelink': 'peixes',
    },
]

def populate():
    for signo in signos:
        signo = Signos.objects.get_or_create(nome=signo['nome'], data=signo['data'], img=signo['img'], nomelink=signo['nomelink'])[0]

if __name__ == "__main__":
    print("populating db...")
    populate()
    print("done!")

