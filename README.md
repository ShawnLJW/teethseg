# TeethSeg

## Environment Setup

Create and activate a conda environment with:

```{bash}
conda env create -f environment.yml
conda activate teethseg
```

All 3d meshes need to be preprocessed with [Manifold](https://github.com/hjwdzh/Manifold) before they can be fed into our model. Set it up with:

```{bash}
git submodule update --init --recursive
mkdir Manifold/build
cd Manifold/build
cmake .. -DC_MAKE_BUILD_TYPE=Release
make
```

## Repositries Referenced

- [MeshMAE](https://github.com/liang3588/MeshMAE)
- [Manifold](https://github.com/hjwdzh/Manifold)
