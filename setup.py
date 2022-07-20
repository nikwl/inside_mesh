try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# triangle hash (efficient mesh intersection)
triangle_hash_module = Extension(
    'libmesh.triangle_hash',
    sources=[
        'libmesh/triangle_hash.pyx'
    ],
    include_dirs=[numpy.get_include()],
    libraries=['m']  # Unix-like specific
)

setup(
    name='libmesh',
    ext_modules=cythonize([triangle_hash_module]),
    packages=['libmesh'],
    install_requires=requirements,
)
