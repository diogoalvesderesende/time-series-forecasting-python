# Setup

Two ways to run these notebooks. Pick one.

- [Google Colab](#google-colab) — nothing to install, free GPU, works on any machine
- [Local](#local-install) — your machine, your environment, more control

If you are not sure, use Colab. That is what the course uses.

---

## Google Colab

### Open a notebook

Click the **Open in Colab** badge at the top of any notebook. That is the whole procedure.

The full index with a badge per notebook is in
[CURRICULUM.md](CURRICULUM.md#every-notebook-one-click).

If you would rather browse from inside Colab: `File → Open notebook → GitHub`, then paste
`https://github.com/diogoalvesderesende/time-series-forecasting-python`.

### The data takes care of itself

Nothing to upload. The first cell of every notebook works out where its data is:

1. **Google Drive**, if you copied the course folder there. This is what the videos show.
2. **The notebook's own folder**, if you cloned the repository.
3. **Downloaded from this repository**, if neither of the above.

Colab's GitHub opener only downloads the `.ipynb` file itself, never the CSVs sitting beside it,
so case 3 is what fires when you click a badge. You will see a short `Downloading ...` line and
then the working directory, and the rest of the notebook runs normally.

One exception worth knowing about: the Python labs use a 36 MB retail file, so their first cell
takes a few seconds longer than the others.

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

Each notebook installs what it needs, pinned to the same version as its folder's
`requirements.txt`. You do not have to do anything.

If a later cell then complains about a version, restart the runtime
(`Runtime → Restart session`) and run again. Colab preloads its own `numpy` and `pandas`, and
they are only swapped out after a restart.

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

The repo is around 100 MB, mostly datasets. Give it a minute.

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
Every notebook is now under GitHub's 5 MB preview limit, so this should not happen. If it does,
read it on the [companion site](https://diogoalvesderesende.github.io/time-series-forecasting-python/)
instead, which renders all of them.

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
