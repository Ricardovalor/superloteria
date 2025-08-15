"""
data_loader.py
Funções mínimas para carregar CSVs de histórico.
Substitua/expanda conforme formato real dos seus arquivos.
"""
from pathlib import Path
import pandas as pd

def load_historico(path: str) -> pd.DataFrame:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")
    return pd.read_csv(p)
