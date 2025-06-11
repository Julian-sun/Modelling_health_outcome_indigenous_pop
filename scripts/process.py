from pathlib import Path
import re
import polars as pl


datasets = Path(__file__).absolute().parent.parent / "datasets"
(datasets / "trusted").mkdir(parents=True, exist_ok=True)

dfs = []
for fcsv in (datasets / "raw").iterdir():
    if (
        (match := re.search(r"\d{1,2}", fcsv.name)) is not None and
        fcsv.name.endswith(".csv")
    ):
        if int(match.group()) in list(range(5, 15)):
            dfs.append(pl.read_csv(fcsv, infer_schema=False))

pl.concat(dfs).write_parquet(
    datasets / "trusted/tuberculose2005_2014.parquet"
)


dfs = []
for fcsv in (datasets / "raw").iterdir():
    if (
        (match := re.search(r"\d{1,2}", fcsv.name)) is not None and
        fcsv.name.endswith(".csv")
    ):
        if int(match.group()) in list(range(15, 25)):
            dfs.append(pl.read_csv(fcsv, infer_schema=False))


pl.concat(dfs).write_parquet(
    datasets / "trusted/tuberculose2015_2024.parquet"
)
