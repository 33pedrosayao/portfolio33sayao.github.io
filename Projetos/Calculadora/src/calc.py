#!/usr/bin/env python3
from typing import Callable, Dict

import operator

OPERADORES: Dict[str, Callable[[float, float], float]] = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "//": operator.floordiv,
    "%": operator.mod,
    "**": operator.pow,
}

def calcular(a: float, op: str, b: float) -> float:
    if op not in OPERADORES:
        raise ValueError(f"Operador inválido: {op}. Use um de {list(OPERADORES.keys())}")
    if op in {"/", "//", "%"} and b == 0:
        raise ZeroDivisionError("Divisão por zero.")
    return OPERADORES[op](a, b)

def main() -> None:
    print("Calculadora simples | ops: +  -  *  /  //  %  **")
    print("Exemplos: 2 * 3  |  10 / 2  |  2 ** 8")
    while True:
        try:
            raw = input("\nDigite: ").strip()
            if raw.lower() in {"q", "quit", "sair", "exit"}:
                print("Saindo. 🚀")
                break

            parts = raw.split()
            if len(parts) != 3:
                print("Formato: <numero> <operador> <numero>  (ex: 7 * 8)")
                continue

            a_str, op, b_str = parts
            a, b = float(a_str.replace(",", ".")), float(b_str.replace(",", "."))
            result = calcular(a, op, b)
            # Saída limpa (inteiro sem .0 quando aplicável)
            if result.is_integer():
                print(int(result))
            else:
                print(result)
        except ValueError as ve:
            print(f"Erro de entrada: {ve}")
        except ZeroDivisionError as zde:
            print(f"Erro: {zde}")
        except Exception as e:
            print(f"Falha não prevista: {e}")

if __name__ == "__main__":
    main()
