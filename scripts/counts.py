from pathlib import Path
import polars as pl
import matplotlib.pyplot as plt
import seaborn as sns


pl.Config().set_tbl_rows(20)
p = Path(__file__).absolute().parent.parent / "datasets/trusted/"


df = pl.read_excel(
    p / "dados_final_consolidado.xlsx",
    columns=["ibge", "uf", "regiao", "data_inicio", "descricao_tipologia"]
).filter(pl.col("data_inicio").dt.year().is_between(2005, 2022))

df = df.with_columns(
    pl.Series([1] * df.shape[0]).alias("c"),
    pl.col("data_inicio").dt.strftime("%Y-%m").alias("Ano Mes")
)


df.pivot(
    index=["Ano Mes"],
    values="c",
    on="descricao_tipologia",
    aggregate_function="sum"
).fill_null(0).sort("Ano Mes").write_csv(p / "count_catastrofes_nac.csv")


df.pivot(
    index=["regiao", "Ano Mes"],
    values="c",
    on="descricao_tipologia",
    aggregate_function="sum"
).fill_null(0).sort("Ano Mes").write_csv(p / "count_catastrofes_reg.csv")


df.pivot(
    index=["uf", "Ano Mes"],
    values="c",
    on="descricao_tipologia",
    aggregate_function="sum"
).fill_null(0).sort("Ano Mes").write_csv(p / "count_catastrofes_uf.csv")


df.pivot(
    index=["ibge", "Ano Mes"],
    values="c",
    on="descricao_tipologia",
    aggregate_function="sum"
).fill_null(0).sort("Ano Mes").write_csv(p / "count_catastrofes_ibge.csv")

df = pl.read_csv(p / "count_catastrofes_nac.csv")
df = df.sort(df.select(pl.col(pl.String)).columns)
print(df)

sns.lineplot(
    x="Ano Mes",
    y="Enxurradas",
    data=df.select("Ano Mes", "Enxurradas").unique().sort("Ano Mes")
)
plt.show()
