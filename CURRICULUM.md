# Curriculum

Full map of **[Master Time Series Analysis and Forecasting with Python](https://www.udemy.com/course/forecasting-python/?referralCode=63045C9CC807EB1EBD9A)** — 39 sections, 397 lectures, 38h 14m of video — and the notebook in this repository that goes with each one.

Sections marked *video only* have no code files. They are introductions, feedback prompts or archived material.

---

## Part 0 — Getting started

| Course section | Length | Repo |
|---|---|---|
| Time Series Analysis and Forecasting with Python | 12m | *video only* |
| AI Diogo, at your disposal | — | *video only* |
| Overview of the AI Time Series Assistant | — | *video only* |

---

## Part 1 — Time Series Analysis

Folder: [`Time Series Analysis/`](Time%20Series%20Analysis)

The foundations. If you skip this part, everything later breaks in ways that are hard to debug.

### Introduction to Time Series Forecasting — 1h 50m

Datetime index, exploratory analysis, resampling, decomposition, seasonality, ACF and PACF.

- `Introduction to Time Series Forecasting.ipynb`
- `Introduction to Time Series Analysis.ipynb`
- `Starter File - Introduction to Time Series Forecasting.ipynb`
- Data: `bitcoin_price.csv`, `choco_monthly_revenue.csv`

### Time Series Analysis Practice — 20m

Three short labs. Data loading and index prep, visualisation, then ACF, PACF and decomposition.

- `Lab 1.ipynb`, `Lab 2.ipynb`, `Lab 3.ipynb` and matching `Starter - Lab N.ipynb`
- Data: `department-sales.csv`

### Python for Time Series Analysis — 53m

Seven labs on a retail dataset. Subsetting, aggregation, weekday patterns, standardising sales, outlier removal, promotion impact.

- `Lab 1 - Starter.ipynb` through `Lab 7 - Starter.ipynb`
- `Labs Complete.ipynb`, `Python for Time Series Analysis.ipynb`
- `Lab 1 - Starter non-Colab.ipynb` for local runs
- Data: `train.csv`, `train.xlsx`

### Exponential Smoothing and Holt-Winters — 1h 36m

Simple exponential smoothing, double, then Holt-Winters with additive and multiplicative seasonality. Explicit frequency setting, train/test split, forecasting 13 weeks ahead.

- `Holt-Winters.ipynb`
- `Exponential Smoothing.ipynb`
- `Starter File - Exponential Smoothing and Holt-Winters.ipynb`
- `Holt-Winters Cheat Sheet.pdf`, `Date Time Frequency.docx`
- Data: `weekly_customer_complaints.csv`, `bitcoin_price.csv`, `choco_monthly_revenue.csv`

### Holt-Winters capstone project: Air miles — 20m

Six tasks plus a bonus. Every task has a worked solution.

- `Starter Code.ipynb` — the six tasks, empty
- `CAPSTONE PROJECT_ Airmiles.ipynb` — the walkthrough
- `Task Solutions/Task 1.ipynb` … `Task 6.ipynb`
- `Holt Winters Challenge.pdf`
- Data: `airmiles.csv`

### ARIMA, SARIMA and SARIMAX — 2h 11m

Stationarity testing, differencing, model selection, seasonal terms, exogenous regressors, cross-validation.

- `ARIMA, SARIMA and SARIMAX.ipynb`
- `Starter File - ARIMA, SARIMA and SARIMAX.ipynb`
- `SARIMAX Cheat Sheet.pdf`
- Data: `daily_revenue.csv`, `future_regressors.csv`, `best_params_sarimax.csv`

---

## Part 2 — Modern time series forecasting

Folder: [`Modern Time Series Forecasting Techniques/`](Modern%20Time%20Series%20Forecasting%20Techniques)

### (Facebook) Prophet — 2h 49m

The longest single model section in the course. Holidays, feature engineering, cross-validation, error analysis, parameter tuning, forecasting forward.

- `Prophet Template.ipynb` — 85 cells, the reference implementation
- Data: `Daily Bike Sharing training.csv`, `Daily Bike Sharing future.csv`
- `Readme.txt` — bike sharing dataset documentation

### Prophet capstone project — 49m

- `Prophet Capstone Project.ipynb`, `Prophet Capstone Project - NEW.ipynb`
- `Prophet Challenge.pdf`
- Data: `DHS_weekly.csv`

### Intermittent Time Series — 1h 14m

Demand that is mostly zeros. Standard metrics lie here, so the section covers what to use instead.

- `Intermittent Time Series.ipynb`
- `Starter File - Intermittent Time Series.ipynb`
- Uses `statsforecast` alongside Darts
- Data: `train.csv`

### LinkedIn Silverkite — 2h 5m

Greykite's Silverkite algorithm, end to end. Listed under "Time Series Analysis Graveyard" in the course, still fully usable.

- `LinkedIn Silverkite.ipynb`
- Data: `nyc_data.csv`, `future.csv`

---

## Part 3 — Deep learning for time series forecasting

Folder: [`Deep Learning for Time Series Forecasting/`](Deep%20Learning%20for%20Time%20Series%20Forecasting)

All built on [Darts](https://unit8co.github.io/darts/). Turn on the GPU.

### RNN and LSTM — 1h 37m

One series. Scaling, windowing, cross-validation, then two separate rounds of parameter tuning.

- `LSTM - One Series.ipynb` — 72 cells
- `Starter File - LSTM - One Series.ipynb`
- Data: `nyc_data.csv`, `future.csv`, `best_params_round1.csv`, `best_params_round2.csv`

### LSTM for multiple time series — 1h 17m

Many series in one model. Time covariates, global training.

- `LSTM - Multiple Series.ipynb`
- `Starter File - LSTM - Multiple Series.ipynb`
- Data: `Hourly-train.csv` (M4 competition)

> This notebook is over GitHub's 5 MB render limit. Open it in Colab or locally.

### Temporal Fusion Transformer (TFT) — 1h 57m

Static covariates, past covariates, future covariates, scaling, cross-validation, tuning, interpretability.

- `TFT - one series.ipynb` — 66 cells
- `Starter File - TFT - one series.ipynb`
- Data: `electricity.csv`, `electricity-future.csv`, `best_params.csv`

### TFT capstone project: multiple series — 51m

- `TFT - multiple series.ipynb`
- `TFT_multiple_series_completed.ipynb`
- `Starter File - TFT - multiple series.ipynb`
- `Project Briefing Temporal Fusion Transformer (TFT) for Time Series Forecasting.pdf`
- Data: `electricity.csv`, `electricity-future.csv`, `forecasts_multi_tft.csv`
- Pins `darts==0.36.0`, unlike the other Darts sections

### N-BEATS — 1h 2m

Interpretable deep learning without feature engineering. Seasonality blocks, covariates, tuning.

- `N-BEATS - one series.ipynb`
- `Starter File - N-BEATS - one series.ipynb`
- Data: `electricity.csv`, `electricity-future.csv`, `best_params.csv`

---

## Part 4 — Advanced content

Folder: [`Advanced Content for Time Series/`](Advanced%20Content%20for%20Time%20Series)

The newest material. Foundation models, AutoML and classification.

### GenAI for time series: Amazon Chronos — 2h 23m

Chronos and Chronos 2. Zero-shot forecasting with no training at all, then past covariates, then multiple series, then cross-validation.

- `Amazon Chronos.ipynb` — 65 cells
- `Starter File - Amazon Chronos - One Series.ipynb`
- Data: Beijing multi-site air quality, loaded through `tsdb`

### Amazon AutoGluon — 1h 7m

AutoML for forecasting. Trains and ensembles AutoETS, DeepAR, TFT, Chronos 2, a fine-tuned Chronos, tabular models and more, then weights them.

- `Amazon AutoGluon.ipynb`
- `Amazon AutoGluon - Starter File.ipynb`
- Covariates and interpretability included
- Data: `australia_library_data.csv`, `australia_library_future.csv`

### Google TSMixer — 1h 9m

All-MLP architecture. Data prep, cross-validation, parameter tuning, forecasting forward.

- `Google TS Mixer.ipynb`
- `Google TS Mixer - Starter File.ipynb`
- Data: `bike data.csv`, `best_params.csv`, `best_params_tsmixer.csv`

### TSMixer project: multivariate — project section

Past covariates, future covariates, scaling, multivariate targets. Comes with a written client briefing, the way a real request arrives.

- `Google TS Mixer - Multivariate.ipynb` — 58 cells
- `Project Briefing_ Coffee.pdf` / `.docx`
- Data: `special_coffee_sales_data.xlsx`, `special_coffee_future.xlsx`

### Classification for time series — 46m

Not forecasting. Given a series, what kind of thing is it? InceptionTime on wearable sensor data.

- `InceptionTime.ipynb`
- `Starter File - InceptionTime.ipynb`
- Data: `BasicMotions`, loaded through `sktime`

### Final capstone: build an automated forecasting pipeline — 1h 26m

The section that ties everything together. One function that takes any dataset and returns a forecast.

- `Building an automated Forecasting Model.ipynb`
- `Automated Time Series Forecasting.ipynb`
- `Build an Automated Time Series Forecasting Model.pdf`
- Data: `Daily Bike Sharing.csv`, `electricity-BE.csv`, `nyc_data.csv` and their future counterparts

---

## Appendix — Python for Data Analysis

Bundled with the course as a full Python primer for anyone who needs it. Video only in this repo.

| Section | Length |
|---|---|
| Python Essentials | 45m |
| Book Review | 10m |
| Variable Types and Operators | 1h 9m |
| If-else and Conditionals | 25m |
| Python Intermediate | 3h 10m |
| Capstone project: Virtual Escape Game | 48m |
| Pandas | 2h 5m |
| Pandas Challenge | 1h 1m |

---

## Reusable code

[`Useful Code  Template.ipynb`](Useful%20Code%20%20Template.ipynb) in the repo root collects the blocks you will paste into every project: setup, visualisation, seasonality checks, ACF and PACF, model assessment, and plotting the future.

---

**[Take the full course on Udemy →](https://www.udemy.com/course/forecasting-python/?referralCode=63045C9CC807EB1EBD9A)**
