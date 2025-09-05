#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Processamento de dados de Tuberculose (SINAN)
------------------------------------------------
Autor: Juliane F. Oliveira
Instituição: Centro de Integração de Dados e Conhecimentos para Saúde (CIDACS/Fiocruz)


Descrição:
    Este script realiza o pré-processamento dos dados de TB (SINAN),
    incluindo:
    - Conversão de tipos e padronização de variáveis
    - Recodificação de valores inválidos e ausentes
    - Exclusão de variáveis irrelevantes
    - Filtragem por período de estudo (2005–2023)
    - Exportação em formato Parquet para análises futuras
"""

import pandas as pd
import numpy as np

# ==========================================================
# 1. Load Data
# ==========================================================
df = pd.read_csv(
    "/Users/julianeoliveira/Documents/Projects/Bruno/Datalake/sinan_TB.csv",
    low_memory=False
)

# ==========================================================
# 2. Basic Processing
# ==========================================================
df = df.assign(
    NU_ANO=df.NU_ANO.astype(int),
    CS_SEXO=df.CS_SEXO.astype(str),
    ones=1
)

# Filter study period and remove invalid sex
df = df[(2001 <= df.NU_ANO) & (df.NU_ANO < 2024)]
df = df[df.CS_SEXO != "I"]

# ==========================================================
# 3. Variable Cleaning
# ==========================================================
def clean_variable(series, invalid_values, nan_values=None, dtype=int):
    """Replace infinities, handle missing values and recode."""
    s = series.replace([np.inf, -np.inf], np.nan)
    if nan_values is not None:
        s = s.replace(nan_values, np.nan)
    s = s.fillna(9) if 9 in invalid_values else s
    s = s.replace(invalid_values, 9)
    return s.astype(dtype)

# --- TB form
df["FORMA"] = clean_variable(df["FORMA"], invalid_values=[0], nan_values=None)

# --- Race/color
df["CS_RACA"] = clean_variable(df["CS_RACA"], invalid_values=[0, 6])

# --- Vulnerable populations
df["POP_LIBER"] = clean_variable(df["POP_LIBER"], invalid_values=[], nan_values=[0, 9])
df["POP_RUA"]   = clean_variable(df["POP_RUA"],   invalid_values=[], nan_values=[0, 9])
df["POP_SAUDE"] = clean_variable(df["POP_SAUDE"], invalid_values=[], nan_values=[0, 3, 9])
df["POP_IMIG"]  = clean_variable(df["POP_IMIG"],  invalid_values=[], nan_values=[0, 3, 9])

# --- Government benefits
df["BENEF_GOV"] = clean_variable(
    df["BENEF_GOV"], invalid_values=[], nan_values=[0, 3, 4, 5, 6, 7, 8, 9]
)

# ==========================================================
# 4. Drop Unnecessary Variables
# ==========================================================
cols_to_drop = [
    "DT_TRANSDM", "DT_TRANSSM", "DT_TRANSRM",
    "DT_TRANSRS", "DT_TRANSSE", "CS_FLXRET", "FLXRECEBI",
    "TRANSF", "UF_TRANSF", "MUN_TRANSF"
]
df.drop(columns=cols_to_drop, inplace=True, errors="ignore")

# ==========================================================
# 5. Final Filter
# ==========================================================
df = df[(df.NU_ANO >= 2005) & (df.FORMA != 9)]

# ==========================================================
# 6. Save Cleaned Dataset
# ==========================================================
df.to_parquet(
    "/Users/julianeoliveira/Documents/Projects/Bruno/Datalake/clean_TB.parquet"
)

print("Processamento concluído. Base limpa salva com sucesso.")
