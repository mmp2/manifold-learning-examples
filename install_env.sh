#!/bin/bash
conda create -n test_env python=3.6 -y
source activate test_env
conda install -c conda-forge -y nose coverage cython=0.29.11 numpy=1.18.1 \
                                scipy=1.5.2 gudhi=3.0.0 pyamg=4.0.0 \
                                scikit-learn h5py plotly matplotlib=3.1.1 \
                                pyflann tqdm mdanalysis umap-learn \
                                tensorboardx slepc4py
conda install -c numba -y numba
conda install -c anaconda -y pandas seaborn natsort sympy scikit-image
pip install molmod
pip install git+https://github.com/mmp2/megaman
