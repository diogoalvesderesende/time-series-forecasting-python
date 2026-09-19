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

---

## Every notebook, one click

Each notebook opens in Google Colab and runs top to bottom. The setup cell finds its
data whether you are on Drive, on a local clone, or opening straight from GitHub.

You can also read any of them as a web page, no Colab needed, on the
[companion site](https://diogoalvesderesende.github.io/time-series-forecasting-python/).

### Part 1 — Time Series Analysis

| Notebook | Section | Open |
|---|---|---|
| [ARIMA, SARIMA and SARIMAX](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/ARIMA%2C%20SARIMA%20and%20SARIMAX/ARIMA%2C%20SARIMA%20and%20SARIMAX.html) | ARIMA, SARIMA and SARIMAX | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/ARIMA%2C%20SARIMA%20and%20SARIMAX/ARIMA%2C%20SARIMA%20and%20SARIMAX.ipynb) |
| [Starter File - ARIMA, SARIMA and SARIMAX](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/ARIMA%2C%20SARIMA%20and%20SARIMAX/Starter%20File%20-%20ARIMA%2C%20SARIMA%20and%20SARIMAX.html) | ARIMA, SARIMA and SARIMAX | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/ARIMA%2C%20SARIMA%20and%20SARIMAX/Starter%20File%20-%20ARIMA%2C%20SARIMA%20and%20SARIMAX.ipynb) |
| [CAPSTONE PROJECT_ Airmiles](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/CAPSTONE%20PROJECT%20-%20Airmiles/CAPSTONE%20PROJECT_%20Airmiles.html) | CAPSTONE PROJECT - Airmiles | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/CAPSTONE%20PROJECT%20-%20Airmiles/CAPSTONE%20PROJECT_%20Airmiles.ipynb) |
| [Starter Code](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/CAPSTONE%20PROJECT%20-%20Airmiles/Starter%20Code.html) | CAPSTONE PROJECT - Airmiles | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/CAPSTONE%20PROJECT%20-%20Airmiles/Starter%20Code.ipynb) |
| [Solutions Udemy Workspace - Airmiles](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/CAPSTONE%20PROJECT%20-%20Airmiles/Task%20Solutions/Solutions%20Udemy%20Workspace%20-%20Airmiles.html) | CAPSTONE PROJECT - Airmiles | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/CAPSTONE%20PROJECT%20-%20Airmiles/Task%20Solutions/Solutions%20Udemy%20Workspace%20-%20Airmiles.ipynb) |
| [Task 1](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/CAPSTONE%20PROJECT%20-%20Airmiles/Task%20Solutions/Task%201.html) | CAPSTONE PROJECT - Airmiles | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/CAPSTONE%20PROJECT%20-%20Airmiles/Task%20Solutions/Task%201.ipynb) |
| [Task 2](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/CAPSTONE%20PROJECT%20-%20Airmiles/Task%20Solutions/Task%202.html) | CAPSTONE PROJECT - Airmiles | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/CAPSTONE%20PROJECT%20-%20Airmiles/Task%20Solutions/Task%202.ipynb) |
| [Task 3](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/CAPSTONE%20PROJECT%20-%20Airmiles/Task%20Solutions/Task%203.html) | CAPSTONE PROJECT - Airmiles | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/CAPSTONE%20PROJECT%20-%20Airmiles/Task%20Solutions/Task%203.ipynb) |
| [Task 4](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/CAPSTONE%20PROJECT%20-%20Airmiles/Task%20Solutions/Task%204.html) | CAPSTONE PROJECT - Airmiles | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/CAPSTONE%20PROJECT%20-%20Airmiles/Task%20Solutions/Task%204.ipynb) |
| [Task 5](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/CAPSTONE%20PROJECT%20-%20Airmiles/Task%20Solutions/Task%205.html) | CAPSTONE PROJECT - Airmiles | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/CAPSTONE%20PROJECT%20-%20Airmiles/Task%20Solutions/Task%205.ipynb) |
| [Task 6](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/CAPSTONE%20PROJECT%20-%20Airmiles/Task%20Solutions/Task%206.html) | CAPSTONE PROJECT - Airmiles | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/CAPSTONE%20PROJECT%20-%20Airmiles/Task%20Solutions/Task%206.ipynb) |
| [Exponential Smoothing](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/Exponential%20Smoothing%20and%20Holt%20Winters/Exponential%20Smoothing.html) | Exponential Smoothing and Holt Winters | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/Exponential%20Smoothing%20and%20Holt%20Winters/Exponential%20Smoothing.ipynb) |
| [Holt-Winters](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/Exponential%20Smoothing%20and%20Holt%20Winters/Holt-Winters.html) | Exponential Smoothing and Holt Winters | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/Exponential%20Smoothing%20and%20Holt%20Winters/Holt-Winters.ipynb) |
| [Starter File - Exponential Smoothing and Holt-Winters](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/Exponential%20Smoothing%20and%20Holt%20Winters/Starter%20File%20-%20Exponential%20Smoothing%20and%20Holt-Winters.html) | Exponential Smoothing and Holt Winters | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/Exponential%20Smoothing%20and%20Holt%20Winters/Starter%20File%20-%20Exponential%20Smoothing%20and%20Holt-Winters.ipynb) |
| [Introduction to Time Series Analysis](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/Introduction%20to%20Time%20Series%20Forecasting/Introduction%20to%20Time%20Series%20Analysis.html) | Introduction to Time Series Forecasting | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/Introduction%20to%20Time%20Series%20Forecasting/Introduction%20to%20Time%20Series%20Analysis.ipynb) |
| [Introduction to Time Series Forecasting](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/Introduction%20to%20Time%20Series%20Forecasting/Introduction%20to%20Time%20Series%20Forecasting.html) | Introduction to Time Series Forecasting | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/Introduction%20to%20Time%20Series%20Forecasting/Introduction%20to%20Time%20Series%20Forecasting.ipynb) |
| [Starter File - Introduction to Time Series Forecasting](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/Introduction%20to%20Time%20Series%20Forecasting/Starter%20File%20-%20Introduction%20to%20Time%20Series%20Forecasting.html) | Introduction to Time Series Forecasting | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/Introduction%20to%20Time%20Series%20Forecasting/Starter%20File%20-%20Introduction%20to%20Time%20Series%20Forecasting.ipynb) |
| [Lab 1 - Starter non-Colab](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/Python%20for%20Time%20Series%20Analysis/Lab%201%20-%20Starter%20non-Colab.html) | Python for Time Series Analysis | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/Python%20for%20Time%20Series%20Analysis/Lab%201%20-%20Starter%20non-Colab.ipynb) |
| [Lab 1 - Starter](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/Python%20for%20Time%20Series%20Analysis/Lab%201%20-%20Starter.html) | Python for Time Series Analysis | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/Python%20for%20Time%20Series%20Analysis/Lab%201%20-%20Starter.ipynb) |
| [Lab 2 - Starter](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/Python%20for%20Time%20Series%20Analysis/Lab%202%20-%20Starter.html) | Python for Time Series Analysis | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/Python%20for%20Time%20Series%20Analysis/Lab%202%20-%20Starter.ipynb) |
| [Lab 3 - Starter](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/Python%20for%20Time%20Series%20Analysis/Lab%203%20-%20Starter.html) | Python for Time Series Analysis | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/Python%20for%20Time%20Series%20Analysis/Lab%203%20-%20Starter.ipynb) |
| [Lab 4 - Starter](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/Python%20for%20Time%20Series%20Analysis/Lab%204%20-%20Starter.html) | Python for Time Series Analysis | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/Python%20for%20Time%20Series%20Analysis/Lab%204%20-%20Starter.ipynb) |
| [Lab 5 - Starter](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/Python%20for%20Time%20Series%20Analysis/Lab%205%20-%20Starter.html) | Python for Time Series Analysis | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/Python%20for%20Time%20Series%20Analysis/Lab%205%20-%20Starter.ipynb) |
| [Lab 6 - Starter](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/Python%20for%20Time%20Series%20Analysis/Lab%206%20-%20Starter.html) | Python for Time Series Analysis | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/Python%20for%20Time%20Series%20Analysis/Lab%206%20-%20Starter.ipynb) |
| [Lab 7 - Starter](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/Python%20for%20Time%20Series%20Analysis/Lab%207%20-%20Starter.html) | Python for Time Series Analysis | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/Python%20for%20Time%20Series%20Analysis/Lab%207%20-%20Starter.ipynb) |
| [Labs Complete](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/Python%20for%20Time%20Series%20Analysis/Labs%20Complete.html) | Python for Time Series Analysis | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/Python%20for%20Time%20Series%20Analysis/Labs%20Complete.ipynb) |
| [Python for Time Series Analysis](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/Python%20for%20Time%20Series%20Analysis/Python%20for%20Time%20Series%20Analysis.html) | Python for Time Series Analysis | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/Python%20for%20Time%20Series%20Analysis/Python%20for%20Time%20Series%20Analysis.ipynb) |
| [Lab 1](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/Time%20Series%20Analysis%20Practice/Lab%201.html) | Time Series Analysis Practice | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/Time%20Series%20Analysis%20Practice/Lab%201.ipynb) |
| [Lab 2](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/Time%20Series%20Analysis%20Practice/Lab%202.html) | Time Series Analysis Practice | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/Time%20Series%20Analysis%20Practice/Lab%202.ipynb) |
| [Lab 3](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/Time%20Series%20Analysis%20Practice/Lab%203.html) | Time Series Analysis Practice | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/Time%20Series%20Analysis%20Practice/Lab%203.ipynb) |
| [Starter - Lab 1](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/Time%20Series%20Analysis%20Practice/Starter%20-%20Lab%201.html) | Time Series Analysis Practice | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/Time%20Series%20Analysis%20Practice/Starter%20-%20Lab%201.ipynb) |
| [Starter - Lab 2](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/Time%20Series%20Analysis%20Practice/Starter%20-%20Lab%202.html) | Time Series Analysis Practice | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/Time%20Series%20Analysis%20Practice/Starter%20-%20Lab%202.ipynb) |
| [Starter - Lab 3](https://diogoalvesderesende.github.io/time-series-forecasting-python/Time%20Series%20Analysis/Time%20Series%20Analysis%20Practice/Starter%20-%20Lab%203.html) | Time Series Analysis Practice | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Time%20Series%20Analysis/Time%20Series%20Analysis%20Practice/Starter%20-%20Lab%203.ipynb) |

### Part 2 — Modern Techniques

| Notebook | Section | Open |
|---|---|---|
| [Prophet Capstone Project - NEW](https://diogoalvesderesende.github.io/time-series-forecasting-python/Modern%20Time%20Series%20Forecasting%20Techniques/CAPSTONE%20PROJECT%20-%20Prophet/Prophet%20Capstone%20Project%20-%20NEW.html) | CAPSTONE PROJECT - Prophet | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Modern%20Time%20Series%20Forecasting%20Techniques/CAPSTONE%20PROJECT%20-%20Prophet/Prophet%20Capstone%20Project%20-%20NEW.ipynb) |
| [Prophet Capstone Project](https://diogoalvesderesende.github.io/time-series-forecasting-python/Modern%20Time%20Series%20Forecasting%20Techniques/CAPSTONE%20PROJECT%20-%20Prophet/Prophet%20Capstone%20Project.html) | CAPSTONE PROJECT - Prophet | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Modern%20Time%20Series%20Forecasting%20Techniques/CAPSTONE%20PROJECT%20-%20Prophet/Prophet%20Capstone%20Project.ipynb) |
| [Intermittent Time Series](https://diogoalvesderesende.github.io/time-series-forecasting-python/Modern%20Time%20Series%20Forecasting%20Techniques/Intermittent%20Time%20Series/Intermittent%20Time%20Series.html) | Intermittent Time Series | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Modern%20Time%20Series%20Forecasting%20Techniques/Intermittent%20Time%20Series/Intermittent%20Time%20Series.ipynb) |
| [Starter File - Intermittent Time Series](https://diogoalvesderesende.github.io/time-series-forecasting-python/Modern%20Time%20Series%20Forecasting%20Techniques/Intermittent%20Time%20Series/Starter%20File%20-%20Intermittent%20Time%20Series.html) | Intermittent Time Series | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Modern%20Time%20Series%20Forecasting%20Techniques/Intermittent%20Time%20Series/Starter%20File%20-%20Intermittent%20Time%20Series.ipynb) |
| [LinkedIn Silverkite](https://diogoalvesderesende.github.io/time-series-forecasting-python/Modern%20Time%20Series%20Forecasting%20Techniques/LinkedIn%20Silverkite/LinkedIn%20Silverkite.html) | LinkedIn Silverkite | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Modern%20Time%20Series%20Forecasting%20Techniques/LinkedIn%20Silverkite/LinkedIn%20Silverkite.ipynb) |
| [Prophet Template](https://diogoalvesderesende.github.io/time-series-forecasting-python/Modern%20Time%20Series%20Forecasting%20Techniques/Prophet/Prophet%20Template.html) | Prophet | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Modern%20Time%20Series%20Forecasting%20Techniques/Prophet/Prophet%20Template.ipynb) |

### Part 3 — Deep Learning

| Notebook | Section | Open |
|---|---|---|
| [Starter File - TFT - multiple series](https://diogoalvesderesende.github.io/time-series-forecasting-python/Deep%20Learning%20for%20Time%20Series%20Forecasting/CAPSTONE%20PROJECT%20-%20TFT%20for%20multiple%20series/Starter%20File%20-%20TFT%20-%20multiple%20series.html) | CAPSTONE PROJECT - TFT for multiple series | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Deep%20Learning%20for%20Time%20Series%20Forecasting/CAPSTONE%20PROJECT%20-%20TFT%20for%20multiple%20series/Starter%20File%20-%20TFT%20-%20multiple%20series.ipynb) |
| [TFT - multiple series](https://diogoalvesderesende.github.io/time-series-forecasting-python/Deep%20Learning%20for%20Time%20Series%20Forecasting/CAPSTONE%20PROJECT%20-%20TFT%20for%20multiple%20series/TFT%20-%20multiple%20series.html) | CAPSTONE PROJECT - TFT for multiple series | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Deep%20Learning%20for%20Time%20Series%20Forecasting/CAPSTONE%20PROJECT%20-%20TFT%20for%20multiple%20series/TFT%20-%20multiple%20series.ipynb) |
| [TFT_multiple_series_completed](https://diogoalvesderesende.github.io/time-series-forecasting-python/Deep%20Learning%20for%20Time%20Series%20Forecasting/CAPSTONE%20PROJECT%20-%20TFT%20for%20multiple%20series/TFT_multiple_series_completed.html) | CAPSTONE PROJECT - TFT for multiple series | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Deep%20Learning%20for%20Time%20Series%20Forecasting/CAPSTONE%20PROJECT%20-%20TFT%20for%20multiple%20series/TFT_multiple_series_completed.ipynb) |
| [LSTM - One Series](https://diogoalvesderesende.github.io/time-series-forecasting-python/Deep%20Learning%20for%20Time%20Series%20Forecasting/LSTM/LSTM%20-%20One%20Series.html) | LSTM | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Deep%20Learning%20for%20Time%20Series%20Forecasting/LSTM/LSTM%20-%20One%20Series.ipynb) |
| [Starter File - LSTM - One Series](https://diogoalvesderesende.github.io/time-series-forecasting-python/Deep%20Learning%20for%20Time%20Series%20Forecasting/LSTM/Starter%20File%20-%20LSTM%20-%20One%20Series.html) | LSTM | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Deep%20Learning%20for%20Time%20Series%20Forecasting/LSTM/Starter%20File%20-%20LSTM%20-%20One%20Series.ipynb) |
| [LSTM - Multiple Series](https://diogoalvesderesende.github.io/time-series-forecasting-python/Deep%20Learning%20for%20Time%20Series%20Forecasting/Multiple%20Series-LSTM/LSTM%20-%20Multiple%20Series.html) | Multiple Series-LSTM | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Deep%20Learning%20for%20Time%20Series%20Forecasting/Multiple%20Series-LSTM/LSTM%20-%20Multiple%20Series.ipynb) |
| [Starter File - LSTM - Multiple Series](https://diogoalvesderesende.github.io/time-series-forecasting-python/Deep%20Learning%20for%20Time%20Series%20Forecasting/Multiple%20Series-LSTM/Starter%20File%20-%20LSTM%20-%20Multiple%20Series.html) | Multiple Series-LSTM | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Deep%20Learning%20for%20Time%20Series%20Forecasting/Multiple%20Series-LSTM/Starter%20File%20-%20LSTM%20-%20Multiple%20Series.ipynb) |
| [N-BEATS - one series](https://diogoalvesderesende.github.io/time-series-forecasting-python/Deep%20Learning%20for%20Time%20Series%20Forecasting/N-BEATS/N-BEATS%20-%20one%20series.html) | N-BEATS | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Deep%20Learning%20for%20Time%20Series%20Forecasting/N-BEATS/N-BEATS%20-%20one%20series.ipynb) |
| [Starter File - N-BEATS - one series](https://diogoalvesderesende.github.io/time-series-forecasting-python/Deep%20Learning%20for%20Time%20Series%20Forecasting/N-BEATS/Starter%20File%20-%20N-BEATS%20-%20one%20series.html) | N-BEATS | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Deep%20Learning%20for%20Time%20Series%20Forecasting/N-BEATS/Starter%20File%20-%20N-BEATS%20-%20one%20series.ipynb) |
| [Starter File - TFT - one series](https://diogoalvesderesende.github.io/time-series-forecasting-python/Deep%20Learning%20for%20Time%20Series%20Forecasting/TFT/Starter%20File%20-%20TFT%20-%20one%20series.html) | TFT | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Deep%20Learning%20for%20Time%20Series%20Forecasting/TFT/Starter%20File%20-%20TFT%20-%20one%20series.ipynb) |
| [TFT - one series](https://diogoalvesderesende.github.io/time-series-forecasting-python/Deep%20Learning%20for%20Time%20Series%20Forecasting/TFT/TFT%20-%20one%20series.html) | TFT | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Deep%20Learning%20for%20Time%20Series%20Forecasting/TFT/TFT%20-%20one%20series.ipynb) |

### Part 4 — Advanced

| Notebook | Section | Open |
|---|---|---|
| [Amazon AutoGluon - Starter File](https://diogoalvesderesende.github.io/time-series-forecasting-python/Advanced%20Content%20for%20Time%20Series/Amazon%20AutoGluon/Amazon%20AutoGluon%20-%20Starter%20File.html) | Amazon AutoGluon | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Advanced%20Content%20for%20Time%20Series/Amazon%20AutoGluon/Amazon%20AutoGluon%20-%20Starter%20File.ipynb) |
| [Amazon AutoGluon](https://diogoalvesderesende.github.io/time-series-forecasting-python/Advanced%20Content%20for%20Time%20Series/Amazon%20AutoGluon/Amazon%20AutoGluon.html) | Amazon AutoGluon | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Advanced%20Content%20for%20Time%20Series/Amazon%20AutoGluon/Amazon%20AutoGluon.ipynb) |
| [InceptionTime](https://diogoalvesderesende.github.io/time-series-forecasting-python/Advanced%20Content%20for%20Time%20Series/Classification%20with%20InceptionTime/InceptionTime.html) | Classification with InceptionTime | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Advanced%20Content%20for%20Time%20Series/Classification%20with%20InceptionTime/InceptionTime.ipynb) |
| [Starter File - InceptionTime](https://diogoalvesderesende.github.io/time-series-forecasting-python/Advanced%20Content%20for%20Time%20Series/Classification%20with%20InceptionTime/Starter%20File%20-%20InceptionTime.html) | Classification with InceptionTime | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Advanced%20Content%20for%20Time%20Series/Classification%20with%20InceptionTime/Starter%20File%20-%20InceptionTime.ipynb) |
| [Automated Time Series Forecasting](https://diogoalvesderesende.github.io/time-series-forecasting-python/Advanced%20Content%20for%20Time%20Series/FINAL%20PROJECT%20-%20Build%20an%20Automated%20Forecasting%20Pipeline/Automated%20Time%20Series%20Forecasting.html) | FINAL PROJECT - Build an Automated Forecasting Pipeline | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Advanced%20Content%20for%20Time%20Series/FINAL%20PROJECT%20-%20Build%20an%20Automated%20Forecasting%20Pipeline/Automated%20Time%20Series%20Forecasting.ipynb) |
| [Building an automated Forecasting Model](https://diogoalvesderesende.github.io/time-series-forecasting-python/Advanced%20Content%20for%20Time%20Series/FINAL%20PROJECT%20-%20Build%20an%20Automated%20Forecasting%20Pipeline/Building%20an%20automated%20Forecasting%20Model.html) | FINAL PROJECT - Build an Automated Forecasting Pipeline | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Advanced%20Content%20for%20Time%20Series/FINAL%20PROJECT%20-%20Build%20an%20Automated%20Forecasting%20Pipeline/Building%20an%20automated%20Forecasting%20Model.ipynb) |
| [Amazon Chronos](https://diogoalvesderesende.github.io/time-series-forecasting-python/Advanced%20Content%20for%20Time%20Series/GenAI%20with%20Amazon%20Chronos/Amazon%20Chronos.html) | GenAI with Amazon Chronos | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Advanced%20Content%20for%20Time%20Series/GenAI%20with%20Amazon%20Chronos/Amazon%20Chronos.ipynb) |
| [Starter File - Amazon Chronos - One Series](https://diogoalvesderesende.github.io/time-series-forecasting-python/Advanced%20Content%20for%20Time%20Series/GenAI%20with%20Amazon%20Chronos/Starter%20File%20-%20Amazon%20Chronos%20-%20One%20Series.html) | GenAI with Amazon Chronos | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Advanced%20Content%20for%20Time%20Series/GenAI%20with%20Amazon%20Chronos/Starter%20File%20-%20Amazon%20Chronos%20-%20One%20Series.ipynb) |
| [Google TS Mixer - Starter File](https://diogoalvesderesende.github.io/time-series-forecasting-python/Advanced%20Content%20for%20Time%20Series/Google%20TS%20Mixer/Google%20TS%20Mixer%20-%20Starter%20File.html) | Google TS Mixer | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Advanced%20Content%20for%20Time%20Series/Google%20TS%20Mixer/Google%20TS%20Mixer%20-%20Starter%20File.ipynb) |
| [Google TS Mixer](https://diogoalvesderesende.github.io/time-series-forecasting-python/Advanced%20Content%20for%20Time%20Series/Google%20TS%20Mixer/Google%20TS%20Mixer.html) | Google TS Mixer | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Advanced%20Content%20for%20Time%20Series/Google%20TS%20Mixer/Google%20TS%20Mixer.ipynb) |
| [Google TS Mixer - Multivariate](https://diogoalvesderesende.github.io/time-series-forecasting-python/Advanced%20Content%20for%20Time%20Series/Project%20-%20Google%20TS%20Mixer/Google%20TS%20Mixer%20-%20Multivariate.html) | Project - Google TS Mixer | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Advanced%20Content%20for%20Time%20Series/Project%20-%20Google%20TS%20Mixer/Google%20TS%20Mixer%20-%20Multivariate.ipynb) |

### Reference

| Notebook | Section | Open |
|---|---|---|
| [Useful Code  Template](https://diogoalvesderesende.github.io/time-series-forecasting-python/Useful%20Code%20%20Template.html) | — | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogoalvesderesende/time-series-forecasting-python/blob/main/Useful%20Code%20%20Template.ipynb) |
