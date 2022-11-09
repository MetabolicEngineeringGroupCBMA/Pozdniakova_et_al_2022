import nbformat


nbs = (
"/home/bjorn/Desktop/mec@github/Pozdniakova_et_al_2022/notebooks/pTA1/ampR.ipynb",
"/home/bjorn/Desktop/mec@github/Pozdniakova_et_al_2022/notebooks/pTA1/pbr.ipynb",
"/home/bjorn/Desktop/mec@github/Pozdniakova_et_al_2022/notebooks/pTA1/2µ.ipynb",
"/home/bjorn/Desktop/mec@github/Pozdniakova_et_al_2022/notebooks/pTA1/LEU2.ipynb",
"/home/bjorn/Desktop/mec@github/Pozdniakova_et_al_2022/notebooks/pTA1/crp∆.ipynb",
)

first_notebook = nbformat.read(nbs[0], 4)

for nb in nbs[1:]:
    next_notebook = nbformat.read(nb, 4)
    first_notebook.cells += next_notebook.cells

nbformat.write(first_notebook, 'final_notebook2.ipynb')
