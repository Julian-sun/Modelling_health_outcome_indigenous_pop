# Aim of this repository

In this repository we provide scripts for collecting, processing and analysing data on tuberculosis (TB). The processed data supports exploratory analyses and the evaluation of mathematical models to infor TB control, prevention, and reduction strategies, particularly in venerable populations. Codes that perform descriptive analyses and modelling are also available here and are described below. In addition to TB data, we also report estimates of population and climate adverse events.

## 🧾 Dataset Description

### TB data

We gathered data on TB from the **Sistema de Informação de Agravos de
Notificação (SINAN)** maintained by the Brazilian Ministry of Health (data
is stored in the Raw folder in our database). The data reports individualised
and unidentified suspected tuberculosis cases, from 2005 to 2023. The following
scripts are used in this step:

1.     script [downloads.py](https://github.com/Julian-sun/Modelling_health_outcome_indigenous_pop/blob/6729b6b6ef1e6c3743ed2e7353cfa5c05287aefc/scripts/downloads.py) is used for downloading data;

2.     script [process.py](https://github.com/Julian-sun/Modelling_health_outcome_indigenous_pop/blob/main/scripts/process.py "process.py") in directory y is used for pre-formatting downloaded data and concatenating it into a single file;

3.     script [process_vars.py](https://github.com/Julian-sun/Modelling_health_outcome_indigenous_pop/blob/main/scripts/process_vars.py "process_vars.py") selects and formats variables that we need for our work.

The resulting data is stored in the Refined folder of our database.



---

#### 📚 TB Variables Dictionary Selected for our Study

##### 1. Notification & Administrative Details

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

##### 2. Demographics

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

##### 3. Clinical & Diagnostic Information

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

##### 4. Comorbidities and Risk Factors

| Variable                                 | Description                                   |
| ---------------------------------------- | --------------------------------------------- |
| `AGRAVAIDS`                              | AIDS                                          |
| `AGRAVALCOO`                             | Alcoholism                                    |
| `AGRAVDIABE`                             | Diabetes                                      |
| `AGRAVDOENC`, `AGRAVOUTRA`, `AGRAVOUTDE` | Other comorbidities (detailed or unspecified) |
| `AGRAVDROGA`                             | Illicit drug use                              |
| `AGRAVTABAC`                             | Tobacco use                                   |

##### 5. Treatment & Medication

| Variable                                                                                    | Description                                   |
| ------------------------------------------------------------------------------------------- | --------------------------------------------- |
| `TRATAMENTO`                                                                                | Treatment type                                |
| `DT_INIC_TR`                                                                                | Treatment start date                          |
| `RIFAMPICIN`, `ISONIAZIDA`, `ETAMBUTOL`, `ESTREPTOMI`, `PIRAZINAMI`, `ETIONAMIDA`, `OUTRAS` | Drugs administered                            |
| `OUTRAS_DES`                                                                                | Other medications (description)               |
| `TRAT_SUPER`, `TRATSUP_AT`                                                                  | Supervised treatment                          |
| `DT_MUDANCA`                                                                                | Treatment change date                         |
| `ANT_RETRO`                                                                                 | Use of antiretrovirals (for HIV co-infection) |

##### 6. Special Populations

| Variable    | Description                  |
| ----------- | ---------------------------- |
| `POP_LIBER` | Incarcerated                 |
| `POP_RUA`   | Homeless                     |
| `POP_SAUDE` | Healthcare workers           |
| `POP_IMIG`  | Immigrants                   |
| `BENEF_GOV` | Receives government benefits |

##### 7. Follow-up & Outcomes

| Variable                                | Description                               |
| --------------------------------------- | ----------------------------------------- |
| `NU_CONTATO`                            | Number of contacts                        |
| `DOENCA_TRA`                            | History of TB treatment                   |
| `SITUA_9_M`, `SITUA_12_M`, `SITUA_ENCE` | Status at 9/12 months and at case closure |
| `DT_ENCERRA`                            | Date of case closure                      |

---

### Climate and disaster events

The climate and disaster events dataset compiles official records classified under the COBRADE system, at the municipal level, across Brazil. Each entry describes an event with information on municipality, state, region, disaster typology and group, as well as start and end dates.

The data were obtained from the Integrated Disaster Information System (S2iD) platform. S2iD brings together various products of the National Secretariat for Protection and Civil Defense, with the aim of improving and providing transparency to risk and disaster management in Brazil through the computerization of processes and the provision of systematized information on that management.

#### 📚 Climate and disaster events Variables Dictionary Selected for our Study

| Coluna                  | Tipo     | Descrição                                                                                 |
| ----------------------- | -------- | ----------------------------------------------------------------------------------------- |
| **id_evento_grupo**     | `string` | Identificador único do evento, combinando código IBGE, código COBRADE e ordem sequencial. |
| **protocolo**           | `string` | Código do protocolo oficial de registro do desastre (ex.: “RO-A-1100015-12200-20070223”). |
| **tipo_documento**      | `string` | Tipo de documento associado ao registro (ex.: A = Avaliação, F = Formulário).             |
| **ibge**                | `int`    | Código do município segundo o IBGE.                                                       |
| **municipio**           | `string` | Nome do município afetado.                                                                |
| **uf**                  | `string` | Unidade da Federação (sigla do estado).                                                   |
| **cobrade**             | `int`    | Código COBRADE (Classificação e Codificação Brasileira de Desastres).                     |
| **regiao**              | `string` | Região geográfica brasileira onde ocorreu o evento (Norte, Nordeste, etc.).               |
| **tipologia**           | `int`    | Código da tipologia do desastre (categoria do COBRADE).                                   |
| **descricao_tipologia** | `string` | Nome da tipologia do evento (ex.: Enxurradas, Chuvas Intensas, Estiagem).                 |
| **grupo_de_desastre**   | `string` | Grupo principal do desastre (ex.: Hidrológico, Meteorológico, Climatológico, Outros).     |
| **data_inicio**         | `date`   | Data de início do evento.                                                                 |
| **data_fim**            | `date`   | Data de término do evento.                                                                |
