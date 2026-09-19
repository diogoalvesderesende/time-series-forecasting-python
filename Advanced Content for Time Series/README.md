# Part 4 — Advanced Content for Time Series

The 2025 and 2026 material.

Foundation models arrived in time series and changed what a baseline looks like. Chronos forecasts a series it has never seen, with no training. That is worth understanding before you spend two days tuning an LSTM.

Part of **[Master Time Series Analysis and Forecasting with Python](https://www.udemy.com/course/forecasting-python/)**.

## Sections

### [GenAI with Amazon Chronos](GenAI%20with%20Amazon%20Chronos)

Chronos and Chronos 2. Zero-shot forecasting first, no training at all. Then past covariates, then multiple series, then cross-validation to see whether it actually holds up.

**Notebooks:** `Amazon Chronos.ipynb` (65 cells), plus a starter file
**Data:** Beijing multi-site air quality, pulled through the `tsdb` library

Needs its own environment. `chronos-forecasting` installs from git and pins `torch==2.6.0`.

### [Amazon AutoGluon](Amazon%20AutoGluon)

AutoML for forecasting. It trains AutoETS, DeepAR, TFT, Chronos 2, a fine-tuned Chronos, tabular models and more, then weights them into an ensemble.

Covariates and interpretability included, so it is not a black box.

**Notebooks:** `Amazon AutoGluon.ipynb`, plus a starter file
**Data:** `australia_library_data.csv`, `australia_library_future.csv`

Running this creates an `AutogluonModels/` folder. It is gitignored. Delete it whenever you like.

### [Google TS Mixer](Google%20TS%20Mixer)

TSMixer. All MLP, no attention, and it holds its own against much heavier architectures. Data prep, cross-validation, parameter tuning, forecasting forward.

**Notebooks:** `Google TS Mixer.ipynb`, plus a starter file
**Data:** `bike data.csv`, `best_params.csv`, `best_params_tsmixer.csv`

### [Project - Google TS Mixer](Project%20-%20Google%20TS%20Mixer)

Multivariate TSMixer on coffee sales. Past covariates, future covariates, scaling, multiple target series.

You get a written client briefing instead of instructions. Read it, decide what to build, then build it.

**Notebooks:** `Google TS Mixer - Multivariate.ipynb` (58 cells)
**Extras:** `Project Briefing_ Coffee.pdf` and `.docx`
**Data:** `special_coffee_sales_data.xlsx`, `special_coffee_future.xlsx`

### [Classification with InceptionTime](Classification%20with%20InceptionTime)

Not forecasting. Given a series, what kind of thing is it? Machine failing or running normally, activity type from a wearable, fraud or not.

InceptionTime on sensor data, through `sktime`.

**Notebooks:** `InceptionTime.ipynb`, plus a starter file
**Data:** `BasicMotions`, loaded through `sktime`

### [FINAL PROJECT - Build an Automated Forecasting Pipeline](FINAL%20PROJECT%20-%20Build%20an%20Automated%20Forecasting%20Pipeline)

The section that ties the whole course together. One function that takes any dataset and returns a forecast, tested against three different datasets.

This is the thing you can actually put to work on Monday.

**Notebooks:** `Building an automated Forecasting Model.ipynb`, `Automated Time Series Forecasting.ipynb`
**Extras:** `Build an Automated Time Series Forecasting Model.pdf`
**Data:** `Daily Bike Sharing.csv`, `electricity-BE.csv`, `nyc_data.csv` and their future counterparts

## Setup

Three separate environments here. They do not mix.

Chronos:

```bash
pip install -r "GenAI with Amazon Chronos/requirements.txt"
```

AutoGluon (pulls around 3 GB, that is normal):

```bash
pip install -r "Amazon AutoGluon/requirements.txt"
```

TSMixer, both sections:

```bash
pip install -r "Google TS Mixer/requirements.txt"
```

InceptionTime and the final project each have their own `requirements.txt` too.

GPU strongly recommended for Chronos and AutoGluon.

Full instructions in [SETUP.md](../SETUP.md).

## Done

That is the course. If it was useful, [leave a review](https://www.udemy.com/course/forecasting-python/) and star this repo.
