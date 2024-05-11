# TeethSeg

## Environment Setup

Create and activate a conda environment with:

```{bash}
conda env create -f environment.yml
conda activate teethseg
```

```{bash}
git submodule update --init --recursive
pip install -e point-transformer/lib/pointops
```
