import sys
from distutils.core import setup, Extension

VERSION = '0.0.4'

EXT_KWDS = dict(name="pylgl",
                sources=["pylgl.c", "lglib.c", "lglopts.c", "lglbnr.c"],
                define_macros=[('NLGLOG', True),
                               ('NCHKSOL', True),
                               ('NLGLDRUPLIG', True),
                               ('NLGLYALSAT', True),
                               ('NLGLFILES', True),
                               ('NLGLDEMA', True)])

if sys.platform != 'win32':
    EXT_KWDS['define_macros'].append(('PYLGL_VERSION', '"%s"' % VERSION))

if '--inplace' in sys.argv:
    EXT_KWDS['define_macros'].append(('DONT_INCLUDE_LGL', True))
    EXT_KWDS['library_dirs'] = ['.']
    EXT_KWDS['libraries'] = ['pylgl']

setup(name="pylgl",
      version=VERSION,
      author="Alexander Feldman",
      author_email="alex@llama.gs",
      url="https://github.com/abfeldman/pylgl",
      license="MIT",
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "Operating System :: OS Independent",
                   "Programming Language :: C",
                   "Programming Language :: Python :: 2",
                   "Programming Language :: Python :: 3",
                   "Topic :: Scientific/Engineering :: Artificial Intelligence",
                   "Topic :: Utilities"],
      ext_modules=[Extension(**EXT_KWDS)],
      py_modules=['test_pylgl'],
      description="bindings to lgl (a SAT solver)",
      long_description=open('README.rst').read())
