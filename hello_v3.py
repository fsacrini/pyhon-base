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
__version__ = "0.1.3"
__author__ = "Fabio Sacrini"
__license__ = "Unlicense"

import os
import sys

arguments = {"lang": None, "count": 1}

for arg in sys.argv[1:]:
    #TODO Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option '{key}'")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    #TODO: Usar repeticao
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language: ")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour Monde!",
    "en_CA" : "Hello, World!",
}

print(
    print(msg[current_language] * int(arguments["count"]))
)