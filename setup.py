"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

try:
    from sphinx.setup_command import BuildDoc
except ImportError as e:
    BuildDoc = None

# To use a consistent encoding
from codecs import open
from os import path
here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requirements = f.read()

with open(path.join(here, 'VERSION.cfg'), encoding='utf-8') as f:
    version = f.read().strip().lower()

from distutils.core import setup
setup(
  name = 'volosAPI',
  packages = ['volosAPI'],
  version = version,
  license='MIT',
  description =  'Volos Portfolio Solutions LLC, Data API Python Integrator',
  long_description = long_description,
  author='Volos Portfolio Solutions',
  author_email='info@volossoftware.com',

  url = 'https://github.com/saif-sultan/volosAPI',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Volos', 'Data API', 'FinTech'],
  install_requires=requirements,
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 2.7'
  ],
)