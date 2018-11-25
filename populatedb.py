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
        'img': '',
        'nomelink': 'aries',
    },
    {
        'nome': 'Touro',
        'data': '21/04 - 20/05',
        'img': '',
        'nomelink': 'touro',
    },
    {
        'nome': 'Gêmeos',
        'data': '21/05 - 20/06',
        'img': '',
        'nomelink': 'gemeos',
    },
    {
        'nome': 'Câncer',
        'data': '21/06 - 21/07',
        'img': '',
        'nomelink': 'cancer',
    },
    {
        'nome': 'Leão',
        'data': '22/07 - 22/08',
        'img': '',
        'nomelink': 'leao',
    },
    {
        'nome': 'Virgem',
        'data': '23/08 - 22/09',
        'img': '',
        'nomelink': 'virgem',
    },
    {
        'nome': 'Libra',
        'data': '23/09 - 22/10',
        'img': '',
        'nomelink': 'libra',
    },
    {
        'nome': 'Escorpião',
        'data': '23/10 - 21/11',
        'img': '',
        'nomelink': 'escorpiao',
    },
    {
        'nome': 'Sagitário',
        'data': '22/11 - 21/12',
        'img': '',
        'nomelink': 'sagitario',
    },
    {
        'nome': 'Capricórnio',
        'data': '22/12 - 20/01',
        'img': '',
        'nomelink': 'capricornio',
    },
    {
        'nome': 'Aquário',
        'data': '21/01 - 19/02',
        'img': '',
        'nomelink': 'aquario',
    },
    {
        'nome': 'Peixes',
        'data': '20/02 - 20/03',
        'img': '',
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

