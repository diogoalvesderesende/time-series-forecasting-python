# Master Time Series Analysis and Forecasting with Python

**Every notebook, dataset and starter file from the Udemy course — in one repository.**

[![Course rating](https://img.shields.io/badge/rating-4.3%20%E2%98%85-f6b100)](https://www.udemy.com/course/forecasting-python/?referralCode=63045C9CC807EB1EBD9A)
[![Reviews](https://img.shields.io/badge/reviews-1%2C545-blue)](https://www.udemy.com/course/forecasting-python/?referralCode=63045C9CC807EB1EBD9A)
[![Students](https://img.shields.io/badge/students-13%2C693-blue)](https://www.udemy.com/course/forecasting-python/?referralCode=63045C9CC807EB1EBD9A)
[![Lectures](https://img.shields.io/badge/lectures-397-555)](https://www.udemy.com/course/forecasting-python/?referralCode=63045C9CC807EB1EBD9A)
[![Runtime](https://img.shields.io/badge/video-38h%2014m-555)](https://www.udemy.com/course/forecasting-python/?referralCode=63045C9CC807EB1EBD9A)
[![Last updated](https://img.shields.io/badge/updated-September%202026-brightgreen)](#update-history)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

👉 **[Take the full course on Udemy](https://www.udemy.com/course/forecasting-python/?referralCode=63045C9CC807EB1EBD9A)**  ·  📖 **[Read the notebooks online](https://diogoalvesderesende.github.io/time-series-forecasting-python/)**

---

## What this is

This is the code repository for **[Master Time Series Analysis and Forecasting with Python](https://www.udemy.com/course/forecasting-python/?referralCode=63045C9CC807EB1EBD9A)**, taught by Diogo Alves de Resende.

Every model in the course has a notebook here.

Most sections ship two versions: a **Starter File** you code along with, and the **completed notebook** with all the outputs.

You do not need the course to use this repo. The notebooks run on their own.

But the *why* behind each line is in the videos.

## The numbers

| | |
|---|---|
| **Rating** | 4.3 out of 5 |
| **Reviews** | 1,545 ratings |
| **Students** | 13,693 enrolled |
| **Content** | 39 sections · 397 lectures · 38h 14m of video |
| **Last updated** | September 2026 |
| **Instructor** | Diogo Alves de Resende — 77,000+ students across all courses |
| **Level** | Beginner friendly. Basic statistics helps (linear regression, p-value) |
| **Language** | Python |

The course has been updated nine times since launch. Full log in [Update history](#update-history).

## What you will build

Every forecasting model in this repo, with the notebook that runs it.

| Model | What it is good at | Folder |
|---|---|---|
| **Exponential Smoothing / Holt-Winters** | Trend and seasonality, fast and explainable | [Time Series Analysis](Time%20Series%20Analysis/Exponential%20Smoothing%20and%20Holt%20Winters) |
| **ARIMA / SARIMA / SARIMAX** | Classic statistical forecasting with external regressors | [Time Series Analysis](Time%20Series%20Analysis/ARIMA%2C%20SARIMA%20and%20SARIMAX) |
| **Prophet** | Strong baselines with holidays and minimal data prep | [Modern Techniques](Modern%20Time%20Series%20Forecasting%20Techniques/Prophet) |
| **Croston and intermittent methods** | Sparse, spiky demand with lots of zeros | [Modern Techniques](Modern%20Time%20Series%20Forecasting%20Techniques/Intermittent%20Time%20Series) |
| **LinkedIn Silverkite** | Flexible regression-based forecasting at scale | [Modern Techniques](Modern%20Time%20Series%20Forecasting%20Techniques/LinkedIn%20Silverkite) |
| **LSTM** | Long-term dependencies, one series or many | [Deep Learning](Deep%20Learning%20for%20Time%20Series%20Forecasting/LSTM) |
| **Temporal Fusion Transformer (TFT)** | Many series, covariates, interpretable attention | [Deep Learning](Deep%20Learning%20for%20Time%20Series%20Forecasting/TFT) |
| **N-BEATS** | Pure deep learning, no feature engineering | [Deep Learning](Deep%20Learning%20for%20Time%20Series%20Forecasting/N-BEATS) |
| **Amazon Chronos and Chronos 2** | Foundation models. Zero-shot forecasting, no training | [Advanced](Advanced%20Content%20for%20Time%20Series/GenAI%20with%20Amazon%20Chronos) |
| **Amazon AutoGluon** | AutoML. Trains and ensembles a dozen models for you | [Advanced](Advanced%20Content%20for%20Time%20Series/Amazon%20AutoGluon) |
| **Google TSMixer** | All-MLP architecture, univariate and multivariate | [Advanced](Advanced%20Content%20for%20Time%20Series/Google%20TS%20Mixer) |
| **InceptionTime** | Time series *classification*, not forecasting | [Advanced](Advanced%20Content%20for%20Time%20Series/Classification%20with%20InceptionTime) |

Plus the parts most tutorials skip: cross-validation for time series, parameter tuning, error analysis, and how to actually predict the future instead of only scoring a test set.

## Repository map

The course runs in four parts. GitHub sorts folders alphabetically, so here is the real order.

### Part 1 — [Time Series Analysis](Time%20Series%20Analysis)

The foundations. Index handling, seasonality, ACF and PACF, stationarity, and the classical models.

- `Introduction to Time Series Forecasting` — index, EDA, decomposition, autocorrelation
- `Time Series Analysis Practice` — 3 guided labs
- `Python for Time Series Analysis` — 7 labs on retail sales data
- `Exponential Smoothing and Holt Winters` — SES through Holt-Winters, plus a cheat sheet PDF
- `CAPSTONE PROJECT - Airmiles` — 6 tasks, full solutions included
- `ARIMA, SARIMA and SARIMAX` — stationarity, differencing, exogenous regressors, cross-validation

### Part 2 — [Modern Time Series Forecasting Techniques](Modern%20Time%20Series%20Forecasting%20Techniques)

Where most real business forecasting actually happens.

- `Prophet` — holidays, feature engineering, cross-validation, tuning
- `CAPSTONE PROJECT - Prophet` — weekly services demand data
- `Intermittent Time Series` — the zero-heavy demand problem
- `LinkedIn Silverkite` — NYC data, end to end

### Part 3 — [Deep Learning for Time Series Forecasting](Deep%20Learning%20for%20Time%20Series%20Forecasting)

Built on [Darts](https://unit8co.github.io/darts/). GPU recommended.

- `LSTM` — one series, two rounds of tuning
- `Multiple Series-LSTM` — M4 hourly, many series at once
- `TFT` — one series with past and future covariates
- `CAPSTONE PROJECT - TFT for multiple series` — electricity load
- `N-BEATS` — one series, covariates, tuning

### Part 4 — [Advanced Content for Time Series](Advanced%20Content%20for%20Time%20Series)

The 2025 and 2026 material. Foundation models and AutoML.

- `GenAI with Amazon Chronos` — Chronos and Chronos 2, zero-shot and with covariates
- `Amazon AutoGluon` — automated ensembling, including a fine-tuned Chronos
- `Google TS Mixer` — univariate, with tuning and cross-validation
- `Project - Google TS Mixer` — multivariate coffee sales, with a written briefing
- `Classification with InceptionTime` — sensor data, sktime
- `FINAL PROJECT - Build an Automated Forecasting Pipeline` — one function, any dataset

### Root

- [`Useful Code  Template.ipynb`](Useful%20Code%20%20Template.ipynb) — the snippets you will reuse in every project: setup, visualisation, seasonality, ACF and PACF, model assessment, plotting the future

## Quick start

### Option 1 — Google Colab (recommended)

Nothing to install. GPU included. **Click the Colab badge at the top of any notebook and run it.**

Every notebook opens and runs top to bottom without setup. The first cell mounts Drive if you
have the course folder there, otherwise it downloads that section's data from this repository.
Nothing to upload, no paths to edit.

A full index with a badge per notebook is in [CURRICULUM.md](CURRICULUM.md#every-notebook-one-click).

For the deep learning notebooks, turn the GPU on first: `Runtime → Change runtime type → T4 GPU`.

### Option 2 — Read it as a web page

Every notebook is also rendered at
**[diogoalvesderesende.github.io/time-series-forecasting-python](https://diogoalvesderesende.github.io/time-series-forecasting-python/)**,
including the large ones GitHub will not preview. No Colab, no clone.

### Option 3 — Local

```bash
git clone https://github.com/diogoalvesderesende/time-series-forecasting-python.git
```

**Install per section, not globally.** Every folder has its own `requirements.txt` because Darts, Prophet, AutoGluon and Chronos pin conflicting versions. One environment for all of them will not work.

```bash
python -m venv .venv-tft
```

```bash
pip install -r "Deep Learning for Time Series Forecasting/TFT/requirements.txt"
```

Full instructions, including Windows notes and the GPU setup, are in [SETUP.md](SETUP.md).

## How to work through it

1. Open the **Starter File** in a section.
2. Watch the lecture and code along.
3. Stuck? Open the completed notebook in the same folder.
4. Do the capstone before moving on. The capstones are where it sticks.

Every section ends the same way: cross-validate, tune, then **predict the future**. That last step is the one most tutorials skip and the one your job actually needs.

## Update history

The course is maintained. This is the log.

| When | What changed |
|---|---|
| **August 2026** | Remade: Introduction to Time Series, Exponential Smoothing, Amazon Chronos. Time Series AI Assistant rebuilt. |
| **September 2025** | All Darts sections re-recorded. New sections: Intermittent Time Series, Classification for Time Series. New projects. Shorter videos by coding with GenAI. |
| **August 2025** | AI Course Assistant launched. |
| **July 2025** | Python Essentials exercises fully updated. |
| **March 2025** | Google TSMixer added. Introduction and Exponential Smoothing tutorials remade. |
| **December 2024** | Amazon AutoGluon added. A `requirements.txt` added to every section. |
| **October 2024** | Amazon Chronos and N-BEATS added. |
| **September 2024** | TFT and the TFT capstone project added. |
| **August 2024** | Course rebuilt 100%. Silverkite, LSTM and projects added. |

Also in [CHANGELOG.md](CHANGELOG.md).

## Who this is for

- Business analysts who need a forecast that holds up in a meeting
- Data scientists moving from tabular ML into time series
- Demand planners and operations managers
- Financial and marketing analysts forecasting revenue or demand
- Anyone who has fit an ARIMA, got a flat line, and wondered what went wrong

## FAQ

**Do I need to buy the course to use this repo?**
No. The notebooks run on their own and the repo is MIT licensed. The course explains the reasoning behind each choice, which is the part that is hard to get from code alone.

**What Python version?**
Python 3.10 or 3.11. The default Colab runtime works for everything here.

**Which libraries does the course use?**
[Darts](https://unit8co.github.io/darts/) for LSTM, TFT, N-BEATS and TSMixer. `statsmodels` for the classical models. `prophet` for Prophet. `statsforecast` for intermittent demand. `greykite` for Silverkite. `autogluon.timeseries` for AutoGluon. `chronos-forecasting` for Chronos. `sktime` for InceptionTime.

**Why does every folder have its own requirements.txt?**
Because the libraries conflict. AutoGluon and Darts want different versions of the same packages. Install per section.

**Do I need a GPU?**
For Part 1 and Part 2, no. For LSTM, TFT, N-BEATS and Chronos, yes if you want it to finish while you are still awake. The free Colab T4 is enough.

**What is the difference between a Starter File and the other notebook?**
The Starter File has the setup and the data loading done, and the modelling left empty. You fill it in during the lecture. The other notebook is the finished version with outputs.

**Can I use these notebooks at work?**
Yes. MIT license. Attribution is appreciated, not required.

**Does the course cover foundation models?**
Yes. Amazon Chronos and Chronos 2 get a full section, including zero-shot forecasting, covariates, cross-validation, and fine-tuning through AutoGluon.

**Is there support?**
Q&A inside the Udemy course, plus an AI Time Series Assistant trained on the course content.

## Datasets

All datasets are public or course-made, and each one sits in the folder that uses it.

| Dataset | Used for | Source |
|---|---|---|
| Bike sharing (daily) | Prophet, automated pipeline | [UCI / Fanaee-T and Gama (2013)](https://doi.org/10.1007/s13748-013-0040-3) |
| Electricity load | TFT, N-BEATS | Public grid data |
| M4 hourly | LSTM multiple series | [M4 Competition](https://github.com/Mcompetitions/M4-methods) |
| NYC data | LSTM, Silverkite | Public city data |
| Airmiles | Holt-Winters capstone | Classic R dataset |
| Retail store sales | Python labs, intermittent demand | Public retail dataset |
| Australia library visits | AutoGluon | Public open data |
| Beijing multi-site air quality | Chronos | Loaded via [`tsdb`](https://github.com/WenjieDu/TSDB) |
| BasicMotions | InceptionTime | Loaded via [`sktime`](https://www.sktime.net/) |
| Bitcoin price, chocolate revenue, customer complaints, daily revenue | Introduction, Holt-Winters, SARIMAX | Course datasets |

## About the instructor

**Diogo Alves de Resende** is a data and AI instructor with 77,000+ students. He spent years in analytics leadership in Berlin, working on revenue planning at scale, and now teaches full time and builds products.

- 🎓 [All courses on Udemy](https://www.udemy.com/user/diogo-resende-2/)
- 🌐 [thedatahero.com](https://thedatahero.com/)
- 📬 [Newsletter, 40k+ readers](https://data-heroes-2.kit.com/)
- 💼 [LinkedIn](https://www.linkedin.com/in/diogoalvesderesende/)

## Other courses by the same instructor

If time series is your entry point, these go next: no-code AI, RAG and LLMs, AI agents, and decision science. All at [thedatahero.com](https://thedatahero.com/).

## Contributing

Found a bug, a broken path, or a library that moved on? [Open an issue](https://github.com/diogoalvesderesende/time-series-forecasting-python/issues). See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Code and notebooks: [MIT](LICENSE).

The video course, slides and narration are not covered by this license and remain the property of the author. Dataset credits and the full scope note are in [NOTICE.md](NOTICE.md).

---

⭐ If this repo saved you time, star it. It helps other people find it.

**[Take the full course →](https://www.udemy.com/course/forecasting-python/?referralCode=63045C9CC807EB1EBD9A)**
