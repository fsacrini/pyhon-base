#!/usr/bin/env python3
""" Separacao de classes por sala

Descricao: O programa ira verificar todos os alunos separado por salas de aula.
Importante que o nome esteja correto e igual.

Usage:
Caso inclua uma nova sala ou uma nova classe, crie uma nova linha no dicionario
alunos ou classes e os alunos tem que estar dentro de uma lista.

Execução

    python3 escola_v3_com_dict.py
"""
__version__ = "0.3.0"
__author__ = "Fabio Sacrini"
__license__ = "Unlicense"

# Dados
alunos = {
    "sala1": ["Erik", "Maria", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"],
}

classes = {
    "ingles": ["Erik", "Maria", "Joana", "Carlos", "Antonio"],
    "musica": ["Erik", "Carlos", "Maria"],
    "danca": ["Gustavo", "Sofia", "Joana", "Antonio"],
}

# Interação entre classes e alunos por sala

for atividade in classes:
    print("{:-^40}".format(atividade.capitalize()))
    print()
    for sala in alunos:
        aluno_por_sala = set(classes[atividade]).intersection(set(alunos[sala]))
        aluno_sala = ', '.join(aluno_por_sala)
        print("{} -> {}".format(sala.capitalize(),aluno_sala))
    print()