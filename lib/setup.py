from distutils.core import setup
from Cython.Build import cythonize
import numpy as np

setup(
    name='ebcubed',
    ext_modules=cythonize("ebcubed.pyx"),
    include_dirs=[np.get_include()],
)

setup(
    name='jaccard',
    ext_modules=cythonize("jaccard.pyx"),
    include_dirs=[np.get_include()],
)

setup(
    name='cfisher',
    ext_modules=cythonize("cfisher.pyx"),
    include_dirs=[np.get_include()],
)
