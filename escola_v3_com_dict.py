#!/usr/bin/env python3
"""
"""


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