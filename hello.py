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
__version__ = "0.0.1"
__author__ = "Fabio Sacrini"
__license__ = "Unlicense"

import os

#Dunder => __SOMETHING__

current_language = "en_US" 
current_language = "pt_BR"
current_language = "it_IT"
current_language = os.getenv("LANG", "en_US")[:5]
msg = "Hello, World!"

#Snake Case = current_language
#Pascal Case = CurrentLanguage

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"

print(msg)
#print('fabio'.upper())
#Print(40 + 82)

#Test