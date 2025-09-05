# Aim of this repository

<style>
</style>

In this repository we provide scripts for collecting, processing and analysing data on tuberculosis (TB). The processed data supports exploratory analyses and the evaluation of mathematical models to infor TB control, prevention, and reduction strategies, particularly in venerable populations. Codes that perform descriptive analyses and modelling are also available here and are described below.  In addition to TB data, we also report estimates of population and climate adverse events.

---

## 🧾 Dataset Description

### TB data

<style>
</style>

We gathered data on TB from the **Sistema de Informação de Agravos de
Notificação (SINAN)** maintained by the Brazilian Ministry of Health (data
is stored in the Raw folder in our database). The data reports individualised
and unidentified suspected tuberculosis cases, from 2005 to 2023. The following
scripts are used in this step:

1.     script x in folder y is used for downloading data;

2.     script x in directory y is used for pre-formatting
downloaded data and concatenating it into a single file;

3.     script x in folder y selects and formats variables that
we need for our work.

The resulting data is stored in the Refined folder of our database.

---

## 📚 Variable Dictionary Selected for our Study

### 1. Notification & Administrative Details

| Variable                                                                           | Description                                       |
| ---------------------------------------------------------------------------------- | ------------------------------------------------- |
| `TP_NOT`                                                                           | Type of notification                              |
| `ID_AGRAVO`                                                                        | Disease code (ICD-10 or SINAN-specific)           |
| `DT_NOTIFIC`                                                                       | Date of notification                              |
| `NU_ANO`                                                                           | Year of notification                              |
| `SG_UF_NOT`                                                                        | State abbreviation of the notification origin     |
| `ID_MUNICIP`                                                                       | Municipality code where the notification was made |
| `ID_REGIONA`                                                                       | Regional health authority code                    |
| `DT_DIGITA`                                                                        | Date of data entry                                |
| `DT_TRANSUS`, `DT_TRANSDM`, `DT_TRANSSM`, `DT_TRANSRM`, `DT_TRANSRS`, `DT_TRANSSE` | Data transfer dates at different levels           |
| `CS_FLXRET`                                                                        | Notification flow return code                     |
| `FLXRECEBI`                                                                        | Whether the return was received                   |
| `MIGRADO_W`                                                                        | Flag for record migration                         |
| `TPUNINOT`                                                                         | Type of unit where notification occurred          |

### 2. Demographics

| Variable                                 | Description                            |
| ---------------------------------------- | -------------------------------------- |
| `ANO_NASC`                               | Year of birth                          |
| `NU_IDADE_N`                             | Age (numeric)                          |
| `CS_SEXO`                                | Sex                                    |
| `CS_GESTANT`                             | Pregnancy status                       |
| `CS_RACA`                                | Race/skin color                        |
| `CS_ESCOL_N`                             | Schooling level                        |
| `SG_UF`, `SG_UF_2`, `SG_UF_AT`           | State codes (residence or other)       |
| `ID_MN_RESI`, `ID_MUNIC_2`, `ID_MUNIC_A` | Municipality of residence or follow-up |
| `ID_RG_RESI`                             | Regional health code of residence      |
| `ID_PAIS`                                | Country of residence                   |

### 3. Clinical & Diagnostic Information

| Variable                                   | Description                      |
| ------------------------------------------ | -------------------------------- |
| `DT_DIAG`                                  | Date of diagnosis                |
| `RAIOX_TORA`                               | Chest X-ray result               |
| `TESTE_TUBE`                               | Tuberculin skin test             |
| `FORMA`                                    | Clinical form of TB              |
| `EXTRAPU1_N`, `EXTRAPU2_N`, `EXTRAPUL_O`   | Specific extrapulmonary TB forms |
| `BACILOSC_E`, `BACILOS_E2`, `BACILOSC_O`   | Bacilloscopy results             |
| `CULTURA_ES`, `CULTURA_OU`                 | Culture results                  |
| `HISTOPATOL`                               | Histopathology result            |
| `TEST_MOLEC`                               | Molecular test result            |
| `TEST_SENSI`                               | Drug sensitivity test            |
| `BACILOSC_1` to `BACILOSC_6`, `BAC_APOS_6` | Follow-up bacilloscopy results   |

### 4. Comorbidities and Risk Factors

| Variable                                 | Description                                   |
| ---------------------------------------- | --------------------------------------------- |
| `AGRAVAIDS`                              | AIDS                                          |
| `AGRAVALCOO`                             | Alcoholism                                    |
| `AGRAVDIABE`                             | Diabetes                                      |
| `AGRAVDOENC`, `AGRAVOUTRA`, `AGRAVOUTDE` | Other comorbidities (detailed or unspecified) |
| `AGRAVDROGA`                             | Illicit drug use                              |
| `AGRAVTABAC`                             | Tobacco use                                   |

### 5. Treatment & Medication

| Variable                                                                                    | Description                                   |
| ------------------------------------------------------------------------------------------- | --------------------------------------------- |
| `TRATAMENTO`                                                                                | Treatment type                                |
| `DT_INIC_TR`                                                                                | Treatment start date                          |
| `RIFAMPICIN`, `ISONIAZIDA`, `ETAMBUTOL`, `ESTREPTOMI`, `PIRAZINAMI`, `ETIONAMIDA`, `OUTRAS` | Drugs administered                            |
| `OUTRAS_DES`                                                                                | Other medications (description)               |
| `TRAT_SUPER`, `TRATSUP_AT`                                                                  | Supervised treatment                          |
| `DT_MUDANCA`                                                                                | Treatment change date                         |
| `ANT_RETRO`                                                                                 | Use of antiretrovirals (for HIV co-infection) |

### 6. Special Populations

| Variable    | Description                  |
| ----------- | ---------------------------- |
| `POP_LIBER` | Incarcerated                 |
| `POP_RUA`   | Homeless                     |
| `POP_SAUDE` | Healthcare workers           |
| `POP_IMIG`  | Immigrants                   |
| `BENEF_GOV` | Receives government benefits |

### 7. Follow-up & Outcomes

| Variable                                | Description                               |
| --------------------------------------- | ----------------------------------------- |
| `NU_CONTATO`                            | Number of contacts                        |
| `DOENCA_TRA`                            | History of TB treatment                   |
| `SITUA_9_M`, `SITUA_12_M`, `SITUA_ENCE` | Status at 9/12 months and at case closure |
| `DT_ENCERRA`                            | Date of case closure                      |

### 8. Transfers & Case Linking

| Variable                  | Description                                            |
| ------------------------- | ------------------------------------------------------ |
| `IN_VINCULA`              | Linked case                                            |
| `TRANSF`                  | Transfer to another unit                               |
| `UF_TRANSF`, `MUN_TRANSF` | State and municipality of transfer                     |
| `NU_COMU_EX`              | No de contatos examinados ≤ No de contatos existentes. |

---
