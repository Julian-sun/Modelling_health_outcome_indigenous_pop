import csv
from pathlib import Path
from dbfread import DBF


datasets = Path(__file__).absolute().parent.parent / "datasets/raw"


for dbf_file in datasets.iterdir():
    if dbf_file.name.endswith(".dbf"):
        dbf = DBF(dbf_file, encoding="iso-8859-1")
        with open(datasets / dbf_file.name.replace(".dbf", ".csv"), "w") as fw:
            writer = csv.DictWriter(fw, dbf.field_names)
            writer.writeheader()
            for row in dbf.records:
                writer.writerow(row)
