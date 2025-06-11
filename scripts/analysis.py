from pathlib import Path
import matplotlib.pyplot as plt
import polars as pl
import statsmodels.formula.api as smf
import altair


pl.Config().set_tbl_rows(20)
pl.Config().set_tbl_cols(20)

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
        pl.col("co_ibge").cast(pl.Int32).alias("co_ibge"),
        pl.col("DT_NOTIFIC").map_elements(lambda x: str(x)[:-3], return_dtype=pl.String).alias("year_month"),
        pl.lit(1).alias("dummy")
    )
)

count = df05_14.group_by(
    ["year_month", "co_ibge"]
).agg(pl.sum("dummy").alias("tuberculose")).sort(by="co_ibge")

pivot_clima = df_clima.pivot(
    index=["data_inicio", "data_fim", "co_ibge"],
    on="descricao_tipologia",
    values="enfermos",
    aggregate_function="sum"
).with_columns(
    pl.col("data_inicio")
    .map_elements(lambda x: str(x)[:-3], return_dtype=pl.String)
    .alias("year_month")
).sort("co_ibge")

merge = count.join(
    pivot_clima,
    on=["year_month", "co_ibge"],
    how="left"
).with_columns(
    (pl.col("data_fim") - pl.col("data_inicio")).alias("diff_dt")
)
merge = merge.rename(
    {col: col.replace(" ", "_").replace("/", "_")  for col in merge.columns}
).filter(pl.col("co_ibge") == 110020)

print(merge)
merge = merge.fill_null(0)
events = merge.columns[5:-1]

merge.to_pandas().plot(x="year_month", y="tuberculose", kind="bar")
plt.show()

"""
events = " + ".join(events)
merge = merge.to_pandas()
formula = f"tuberculose ~ {events} + C(co_ibge) + C(DT_NOTIFIC)"
mod = smf.ols(formula, data=merge).fit(cov_type="cluster", cov_kwds={"groups": merge["co_ibge"]})
print(mod.summary())


# for col in df2.columns[2:]:
#     plt.plot(df2.select("DT_NOTIFIC"), df2.select(col))
#     plt.title(f"{col}")
#     plt.show()
"""
