"""
estatisticas.py
Funções estatísticas auxiliares: frequências, médias, tempos entre ocorrências.
"""

from collections import Counter
from typing import List


def frequencia(numeros: List[int]) -> Counter:
    return Counter(numeros)
