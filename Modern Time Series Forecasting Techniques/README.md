# Part 2 — Modern Time Series Forecasting Techniques

Where most real business forecasting actually happens.

Prophet is the model you will reach for when someone needs a number by Friday. Intermittent demand is the problem nobody warns you about until you hit it.

Part of **[Master Time Series Analysis and Forecasting with Python](https://www.udemy.com/course/forecasting-python/)**.

## Sections

### [Prophet](Prophet)

The longest single-model section in the course, and worth it. Holidays, feature engineering, cross-validation, digging into where the error actually comes from, then parameter tuning.

`Prophet Template.ipynb` is 85 cells. It is the reference implementation you will copy into your own projects.

**Data:** `Daily Bike Sharing training.csv`, `Daily Bike Sharing future.csv`
**Extras:** `Readme.txt` documents the bike sharing dataset

### [CAPSTONE PROJECT - Prophet](CAPSTONE%20PROJECT%20-%20Prophet)

Weekly services demand. Build it, tune it, defend it.

**Notebooks:** `Prophet Capstone Project.ipynb`, `Prophet Capstone Project - NEW.ipynb`
**Extras:** `Prophet Challenge.pdf`
**Data:** `DHS_weekly.csv`

### [Intermittent Time Series](Intermittent%20Time%20Series)

Demand that is mostly zeros, with occasional spikes. Spare parts, slow-moving SKUs, niche products.

Standard accuracy metrics lie on this kind of data. A model that predicts zero forever scores well and is useless. This section covers what to do instead.

**Notebooks:** `Intermittent Time Series.ipynb`, plus a starter file
**Libraries:** `statsforecast` and `darts`
**Data:** `train.csv`

### [LinkedIn Silverkite](LinkedIn%20Silverkite)

Greykite's Silverkite algorithm, end to end. Flexible, regression-based, built at LinkedIn for forecasting at scale.

**Notebooks:** `LinkedIn Silverkite.ipynb`
**Data:** `nyc_data.csv`, `future.csv`

## Setup

No GPU needed, but the environments here do not mix. Prophet and Greykite pin conflicting versions.

Prophet sections:

```bash
pip install -r "Prophet/requirements.txt"
```

Silverkite:

```bash
pip install -r "LinkedIn Silverkite/requirements.txt"
```

Intermittent:

```bash
pip install -r "Intermittent Time Series/requirements.txt"
```

On Windows, `prophet` compiles a Stan model and often fails under pip. Use `conda install -c conda-forge prophet` or run it in Colab. `greykite` needs Python 3.10.

Full instructions in [SETUP.md](../SETUP.md).

## Next

[Part 3 — Deep Learning for Time Series Forecasting](../Deep%20Learning%20for%20Time%20Series%20Forecasting)
