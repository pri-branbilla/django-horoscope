# Horóscopo

### Descrição

Como o próprio nome já diz, é uma aplicação web que mostra o horóscopo para o dia. Os resultados são pegos do site da UOL via AJAX.

Esse projeto é meio antigo (de 2016), e resolvi deixar público depois de atualizar as dependências.

## Setup

Siga os próximos passos:

### Virtual environment

```
virtualenv venv
source venv/bin/activate
```

### Instalando dependências

```
pip install -r requirements.txt
```

### Populando o banco de dados

`python populatedb.py`

### Executando

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```
