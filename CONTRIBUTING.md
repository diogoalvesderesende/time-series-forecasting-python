# Contributing

Thanks for looking.

This repo is the companion code for a course, so it is not a general-purpose library. That shapes what is useful to contribute.

## Very welcome

- **Broken things.** A path that does not resolve, a notebook that will not open, a typo in a markdown cell.
- **Library drift.** A package released a breaking change and a notebook now fails. Tell me the version and the error.
- **Environment reports.** "This section works on Python 3.12 with these pins" is genuinely useful.
- **Clearer explanations** in the markdown cells.

## Please do not

- Reformat notebooks wholesale. The diffs are unreadable and the cell order matters for the lectures.
- Swap a model for your preferred one. The model choice follows the curriculum.
- Add new dependencies to an existing `requirements.txt` without a reason tied to a failing notebook.

## How to report a problem

[Open an issue](https://github.com/diogoalvesderesende/time-series-forecasting-python/issues) with:

1. The notebook path
2. The cell that failed
3. The full error
4. `python --version` and the output of `pip freeze | grep <the library>`
5. Colab or local

## Pull requests

- One section per pull request.
- Clear the output of any notebook you touch, unless the output is the point of the change:
  ```bash
  jupyter nbconvert --clear-output --inplace "path/to/notebook.ipynb"
  ```
- Say in the description which notebook you ran end to end to verify the change.

## Questions about the course itself

Those belong in the Udemy Q&A, not here. You will get a faster answer, and other students see it.

[Course Q&A](https://www.udemy.com/course/forecasting-python/)
