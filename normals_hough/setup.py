# from distutils.core import setup
# from distutils.extension import Extension

from setuptools import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy
import platform

DEBUG = False

LINK_ARGS = ['-lgomp']

if platform.system() == 'Windows':
  COMPILE_ARGS = ["/openmp", "/std:c11"]
  
  if DEBUG:
    COMPILE_ARGS.append('/Z7')
    LINK_ARGS.append('/DEBUG')
  
else:
  COMPILE_ARGS = ["-fopenmp", "-std=c++11"]



setup(
    name = "Hough Normal Estimator",
    ext_modules = [
      Extension(
        "NormalEstimatorHough",
        sources=[
          "src/NormalEstimatorHough.pyx",
          "src/normEstHough.cxx"
        ],
        include_dirs=["third_party_includes/", numpy.get_include()],
        language="c++",
        extra_compile_args = COMPILE_ARGS,
        extra_link_args = LINK_ARGS
    )],
    cmdclass = {'build_ext': build_ext},
)
