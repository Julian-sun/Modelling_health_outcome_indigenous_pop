import ftplib
from pathlib import Path


datasets = Path(__file__).absolute().parent.parent / "datasets/raw"
datasets.mkdir(parents=True, exist_ok=True)

ftp = ftplib.FTP("ftp.datasus.gov.br")
ftp.login()

pastas = [
    "/dissemin/publicos/SINAN/DADOS/FINAIS/",
    "/dissemin/publicos/SINAN/DADOS/PRELIM/"
]


for pasta in pastas:
    ftp.cwd(pasta)
    for f_dbc in ftp.nlst():
        if f_dbc.startswith("TUBEBR"):
            with open(datasets / f_dbc, "wb") as fwb:
                ftp.retrbinary(f"RETR {pasta}/{f_dbc}", fwb.write)

ftp.quit()
