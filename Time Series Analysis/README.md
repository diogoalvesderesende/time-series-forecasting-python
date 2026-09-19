# Part 1 — Time Series Analysis

The foundations.

This is the part people want to skip. Do not skip it. Every strange result later in the course traces back to something in here: a wrong index, an unset frequency, a seasonality you did not check for.

Part of **[Master Time Series Analysis and Forecasting with Python](https://www.udemy.com/course/forecasting-python/)**.

## Sections

### [Introduction to Time Series Forecasting](Introduction%20to%20Time%20Series%20Forecasting)

Datetime index, exploratory analysis, resampling, decomposition, seasonality, ACF and PACF. Everything else is built on this.

**Notebooks:** `Introduction to Time Series Forecasting.ipynb`, `Introduction to Time Series Analysis.ipynb`, plus a starter file
**Data:** `bitcoin_price.csv`, `choco_monthly_revenue.csv`

### [Time Series Analysis Practice](Time%20Series%20Analysis%20Practice)

Three short labs to make the concepts stick. Loading and index prep, visualisation, then ACF, PACF and decomposition.

**Notebooks:** `Lab 1.ipynb` to `Lab 3.ipynb` with matching starters
**Data:** `department-sales.csv`

### [Python for Time Series Analysis](Python%20for%20Time%20Series%20Analysis)

Seven labs on real retail sales. Subsetting stores, aggregations, weekday patterns, standardising sales for comparison, removing outliers, measuring promotion impact.

**Notebooks:** `Lab 1 - Starter.ipynb` to `Lab 7 - Starter.ipynb`, `Labs Complete.ipynb`
**Data:** `train.csv`, `train.xlsx`

There is a `Lab 1 - Starter non-Colab.ipynb` if you are running locally.

### [Exponential Smoothing and Holt Winters](Exponential%20Smoothing%20and%20Holt%20Winters)

Simple exponential smoothing, then double, then Holt-Winters with additive and multiplicative seasonality. Setting an explicit frequency, splitting train and test, forecasting 13 weeks out.

**Notebooks:** `Holt-Winters.ipynb`, `Exponential Smoothing.ipynb`, plus a starter file
**Extras:** `Holt-Winters Cheat Sheet.pdf`, `Date Time Frequency.docx`
**Data:** `weekly_customer_complaints.csv`, `bitcoin_price.csv`, `choco_monthly_revenue.csv`

### [CAPSTONE PROJECT - Airmiles](CAPSTONE%20PROJECT%20-%20Airmiles)

Six tasks, done on your own, with a solution notebook for each one.

Open `Starter Code.ipynb`, work through the tasks, and only then look at `Task Solutions/`.

**Extras:** `Holt Winters Challenge.pdf`
**Data:** `airmiles.csv`

### [ARIMA, SARIMA and SARIMAX](ARIMA%2C%20SARIMA%20and%20SARIMAX)

The classical workhorse. Stationarity testing, differencing, choosing p, d and q, adding seasonal terms, then adding external regressors with SARIMAX. Ends with cross-validation.

**Notebooks:** `ARIMA, SARIMA and SARIMAX.ipynb` (76 cells), plus a starter file
**Extras:** `SARIMAX Cheat Sheet.pdf`
**Data:** `daily_revenue.csv`, `future_regressors.csv`

## Setup

No GPU needed for any of this. One environment covers the whole part:

```bash
pip install -r "ARIMA, SARIMA and SARIMAX/requirements.txt"
```

Core libraries: `pandas`, `numpy`, `matplotlib`, `statsmodels`, `scikit-learn`.

Full instructions in [SETUP.md](../SETUP.md).

## Next

[Part 2 — Modern Time Series Forecasting Techniques](../Modern%20Time%20Series%20Forecasting%20Techniques)
