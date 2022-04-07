#!/usr/bin/env python3
""" Nome do Programa: Hello World Multi Linguas.

Até coluna 80
Descricao: Depenendo da lingua configurada no ambiente o programa exibe a 
mensagem correspondende.

Usage:
Tenha a váriavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execução

    python3 hello.py
    or
    ./hello.py
"""
__version__ = "0.1.2"
__author__ = "Fabio Sacrini"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    "en_US": "Hello, World",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour Monde!",
}

print(msg[current_language])