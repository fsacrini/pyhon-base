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

#Dunder => __SOMETHING__

current_language = os.getenv("LANG", "en_US")[:5]
msg = "Hello, World!"

#Snake Case = current_language
#Pascal Case = CurrentLanguage

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"

print(msg)
#print('fabio'.upper())
#Print(40 + 82)

#Test

# Tipos de Print
nome = "Fabio"
print(f"Olá, {nome}")
print("Olá, " + nome)
print("Olá, %s" %nome)
print("Olá, {}".format(nome))
