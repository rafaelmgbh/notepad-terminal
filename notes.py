"""Bloco de notas

$notes.py new "Minha Nota"
tag: tech
text: 
Anotação geral sobre carreira de tecnologia 

$ notes.py read --tag=tech

...
...
"""
__version__ = "0.1.0"

import os
import sys

cmds = ('read', 'new')
path = os.curdir
filepath = os.path.join(path,'notes.txt')

arguments = sys.argv[1:]
if not arguments:
    print('Uso Inválido')
    print(f"Voce precisa especificar o comando {cmds}")
    sys.exit(1)


if arguments[0] not in cmds:
    print(f"Comando inválido {arguments[0]}")

if arguments[0] == 'read':
    pass

if arguments[0] == 'new':
    titulo = arguments[1] # TODO: tratar expection
    text = [
        f"{titulo}\n",
        input('tag:').strip(),
        input('text:\n').strip()
    ]

    with open (filepath, 'a') as file_:
        file_.write("\t".join(text))
