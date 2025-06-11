from pathlib import Path
import matplotlib.pyplot as plt
import polars as pl


pl.Config().set_tbl_rows(20)

datasets = Path(__file__).absolute().parent.parent / "datasets/trusted/"

columns_tube = [
    "DT_NOTIFIC",
    "ID_MN_RESI",
    "CS_SEXO",
    "SITUA_ENCE",
    "POP_RUA",
]

df05_14 = pl.read_parquet(
    datasets / "tuberculose2005_2014.parquet",
    columns=columns_tube
)

df_clima = (
    pl.read_excel(datasets / "dados_final_consolidado.xlsx")
    .sort(by="data_inicio")
).with_columns(
    (pl.col("ibge") // 10).cast(pl.Int32).alias("co_ibge")
)

df05_14 = (
    df05_14.with_columns(
        pl.col("DT_NOTIFIC").cast(pl.Date).alias("DT_NOTIFIC")
    )
    .sort(by="DT_NOTIFIC")
    .rename({"ID_MN_RESI": "co_ibge"})
    .with_columns(
        pl.col("co_ibge").cast(pl.Int32).alias("co_ibge")
    )
)

count = df05_14.group_by(
    ["DT_NOTIFIC", "co_ibge"]
).len().rename({"len": "cases"})

merge = df05_14.join_asof(
    df_clima,
    by="co_ibge",
    left_on="DT_NOTIFIC",
    right_on="data_inicio",
    strategy="backward"
).filter(
    (pl.col("DT_NOTIFIC") <= pl.col("data_fim")) &
    (pl.col("data_inicio") != pl.col("data_fim"))
).join(count, on=["co_ibge", "DT_NOTIFIC"], how="left")


df1 = merge.select(
    "DT_NOTIFIC",
    "ibge",
    "data_inicio",
    "data_fim",
    "descricao_tipologia",
    "grupo_de_desastre",
    "obitos",
    "feridos",
    "enfermos",
    "SITUA_ENCE",
    "co_ibge",
    "CS_SEXO",
    "POP_RUA",
    "cases"
)
print(df1)

df2 = df1.pivot(
        index=["DT_NOTIFIC", "ibge"],
        values="cases",
        on="descricao_tipologia",
        aggregate_function="sum"
)

for col in df2.columns[2:]:
    plt.plot(data=df2, scalex="DT_NOTIFIC", scaley=col, kind="line")
    plt.show()
