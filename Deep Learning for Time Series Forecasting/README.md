# Part 3 — Deep Learning for Time Series Forecasting

Neural networks for forecasting, all built on [Darts](https://unit8co.github.io/darts/).

This is where covariates start to matter. Past covariates, future covariates, static covariates. Get those right and the models do the rest.

**Turn the GPU on before you start.**

Part of **[Master Time Series Analysis and Forecasting with Python](https://www.udemy.com/course/forecasting-python/)**.

## Sections

### [LSTM](LSTM)

One series, done properly. Scaling, windowing, cross-validation, then two separate rounds of parameter tuning because the first round never gets you there.

**Notebooks:** `LSTM - One Series.ipynb` (72 cells), plus a starter file
**Data:** `nyc_data.csv`, `future.csv`, `best_params_round1.csv`, `best_params_round2.csv`

### [Multiple Series-LSTM](Multiple%20Series-LSTM)

One model, many series. This is what you need in production, where you have 4,000 SKUs and nobody is fitting 4,000 models by hand.

**Notebooks:** `LSTM - Multiple Series.ipynb`, plus a starter file
**Data:** `Hourly-train.csv` from the M4 competition

> `LSTM - Multiple Series.ipynb` is larger than GitHub's 5 MB preview limit and will not render in the browser. Open it in Colab or clone the repo.

### [TFT](TFT)

Temporal Fusion Transformer. The strongest general-purpose deep learning model in the course, and the most interpretable. Static covariates, past covariates, future covariates, scaling, cross-validation, tuning.

**Notebooks:** `TFT - one series.ipynb` (66 cells), plus a starter file
**Data:** `electricity.csv`, `electricity-future.csv`, `best_params.csv`

### [CAPSTONE PROJECT - TFT for multiple series](CAPSTONE%20PROJECT%20-%20TFT%20for%20multiple%20series)

TFT across many electricity load series at once. Comes with a written briefing, the way a real request arrives.

**Notebooks:** `Starter File - TFT - multiple series.ipynb`, `TFT - multiple series.ipynb`, `TFT_multiple_series_completed.ipynb`
**Extras:** `Project Briefing Temporal Fusion Transformer (TFT) for Time Series Forecasting.pdf`
**Data:** `electricity.csv`, `electricity-future.csv`, `forecasts_multi_tft.csv`

Note this section pins `darts==0.36.0` while the others pin `0.45.0`. If a cell fails on an unexpected keyword argument, that is the reason.

### [N-BEATS](N-BEATS)

Pure deep learning with no feature engineering, and still interpretable through its trend and seasonality blocks.

**Notebooks:** `N-BEATS - one series.ipynb`, plus a starter file
**Data:** `electricity.csv`, `electricity-future.csv`, `best_params.csv`

## Setup

### Colab

`Runtime → Change runtime type → T4 GPU`, then:

```python
!pip install -q -r requirements.txt
```

Restart the runtime afterwards. Colab ships older `numpy` and `pandas` and they only get replaced after a restart.

### Local

```bash
pip install -r "TFT/requirements.txt"
```

That covers LSTM, Multiple Series-LSTM, TFT and N-BEATS. The TFT capstone needs its own environment because of the Darts version.

Check your GPU is visible:

```python
import torch; print(torch.cuda.is_available())
```

`False` means these notebooks will take hours instead of minutes.

Full instructions in [SETUP.md](../SETUP.md).

## Next

[Part 4 — Advanced Content for Time Series](../Advanced%20Content%20for%20Time%20Series)
