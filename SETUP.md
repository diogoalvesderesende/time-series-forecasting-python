# Setup

Two ways to run these notebooks. Pick one.

- [Google Colab](#google-colab) — nothing to install, free GPU, works on any machine
- [Local](#local-install) — your machine, your environment, more control

If you are not sure, use Colab. That is what the course uses.

---

## Google Colab

### Open a notebook

1. Go to [colab.research.google.com](https://colab.research.google.com/)
2. `File → Open notebook → GitHub`
3. Paste: `https://github.com/diogoalvesderesende/time-series-forecasting-python`
4. Pick the notebook you want

### Get the data in

Most notebooks read a CSV sitting next to them, for example `pd.read_csv('electricity.csv')`. Colab does not see your GitHub folder, so you have to put the file there yourself. Two options.

**Upload it** (fastest for one file):

```python
from google.colab import files
files.upload()
```

**Pull it straight from GitHub** (better, nothing to click):

```python
import urllib.parse, urllib.request

RAW = "https://raw.githubusercontent.com/diogoalvesderesende/time-series-forecasting-python/main/"
path = "Deep Learning for Time Series Forecasting/TFT/electricity.csv"

urllib.request.urlretrieve(RAW + urllib.parse.quote(path), path.split("/")[-1])
```

The `quote` matters. The folder names have spaces in them.

### Turn the GPU on

For LSTM, TFT, N-BEATS, TSMixer, Chronos and AutoGluon:

`Runtime → Change runtime type → T4 GPU → Save`

Check it worked:

```python
import torch
print(torch.cuda.is_available())
```

`False` means you are on CPU and the deep learning sections will take hours instead of minutes.

### Install the libraries

Each folder has a `requirements.txt`. In Colab:

```python
!pip install -q -r requirements.txt
```

Then **restart the runtime** (`Runtime → Restart session`) before you run the rest. Colab preloads older versions of `numpy` and `pandas`, and they only get swapped out after a restart.

---

## Local install

### Prerequisites

- Python 3.10 or 3.11 (3.12 is untested for the deep learning sections)
- Git
- 8 GB RAM minimum, 16 GB for the deep learning sections
- A CUDA GPU for Part 3 and Part 4, or patience

### Clone

```bash
git clone https://github.com/diogoalvesderesende/time-series-forecasting-python.git
```

The repo is around 155 MB, mostly datasets. Give it a minute.

### One environment per section

This is the important part.

Darts, Prophet, AutoGluon, Greykite and Chronos pin conflicting versions of `numpy`, `pandas`, `scikit-learn` and `torch`. There is no single environment that runs all of them. Do not try to build one.

Make an environment per section instead:

```bash
python -m venv .venv-tft
```

Activate it. macOS and Linux:

```bash
source .venv-tft/bin/activate
```

Windows PowerShell:

```powershell
.venv-tft\Scripts\Activate.ps1
```

Install that section's pins:

```bash
pip install -r "Deep Learning for Time Series Forecasting/TFT/requirements.txt"
```

Register the environment as a Jupyter kernel so you can switch between them:

```bash
pip install ipykernel
```

```bash
python -m ipykernel install --user --name tft --display-name "Python (TFT)"
```

Launch:

```bash
jupyter lab
```

Then pick the right kernel in the notebook: `Kernel → Change kernel`.

### The four environments you actually need

Most sections share pins. In practice four environments cover the whole repo.

| Environment | Covers | Install from |
|---|---|---|
| `classic` | Introduction, Practice labs, Python labs, Holt-Winters, Airmiles capstone, ARIMA/SARIMAX | `Time Series Analysis/ARIMA, SARIMA and SARIMAX/requirements.txt` |
| `prophet` | Prophet, Prophet capstone | `Modern Time Series Forecasting Techniques/Prophet/requirements.txt` |
| `darts` | LSTM, Multiple-series LSTM, TFT, N-BEATS, TSMixer, Intermittent | `Deep Learning for Time Series Forecasting/TFT/requirements.txt` |
| `greykite` | Silverkite, Final automated pipeline | `Modern Time Series Forecasting Techniques/LinkedIn Silverkite/requirements.txt` |

Two sections need their own environment and will not share:

- **Amazon Chronos** — `chronos-forecasting` from git, `torch==2.6.0`
- **Amazon AutoGluon** — `autogluon==1.3.1`, `torch==2.2.2`

Also note the TFT capstone pins `darts==0.36.0` while the other Darts sections pin `0.45.0`. If a cell in the capstone fails on an API change, that is why.

---

## Known friction

**`prophet` fails to install on Windows.**
It compiles a Stan model. Install it with conda instead:
```bash
conda install -c conda-forge prophet
```
Or use Colab.

**`greykite` refuses to install on Python 3.12.**
It is pinned to older `numpy` and `scikit-learn`. Use Python 3.10 for those two sections.

**`autogluon` pulls 3 GB of dependencies.**
That is expected. Give it time and disk space.

**`ModuleNotFoundError` right after a successful `pip install` in Colab.**
Restart the runtime. Colab caches the old version in memory.

**A `darts` cell fails with a `TypeError` on a keyword argument.**
The Darts API moved. Check the pinned version in that folder's `requirements.txt` against what you have installed.

**A notebook will not open on github.com.**
`LSTM - Multiple Series.ipynb` is over GitHub's 5 MB render limit. Open it in Colab or clone the repo and open it locally.

**`AutogluonModels/` reappears and is not in git.**
Correct. It is generated when you run the AutoGluon notebook, and it is in `.gitignore`. Delete it freely.

---

## Verify your install

Run this in a fresh notebook cell. It should print versions with no errors.

```python
import sys, pandas, numpy, matplotlib, statsmodels
print("python     ", sys.version.split()[0])
print("pandas     ", pandas.__version__)
print("numpy      ", numpy.__version__)
print("matplotlib ", matplotlib.__version__)
print("statsmodels", statsmodels.__version__)
```

For the Darts sections, add:

```python
import darts, torch
print("darts", darts.__version__, "| torch", torch.__version__, "| cuda", torch.cuda.is_available())
```

---

Still stuck? [Open an issue](https://github.com/diogoalvesderesende/time-series-forecasting-python/issues) with your Python version, the section, and the full error.
