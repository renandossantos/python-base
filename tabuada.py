#!/usr/bin/env python3
"""Hello, World Multi Linguas.

Dependendo da língua configurada no ambiente o programa exibe a mensagem correspondente.

Usage:

Tenha a variável LANG devidamente configurada ex:

    export: LANG=pt_BR

Execução:
    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.1"
__author__ =  "renandossantos"
__license__ = "Unlicense"


numeros = list(range(1,11))

for n1 in numeros:
    print("{:-^18}".format(f"tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print()

    print("#" * 18)
    print()