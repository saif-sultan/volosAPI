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
from package import Package
here = path.abspath(path.dirname(__file__))


def discover_and_run_tests():
    import os
    import sys
    import unittest

    # get setup.py directory
    setup_file = sys.modules['__main__'].__file__
    setup_dir = os.path.abspath(os.path.dirname(setup_file))+"/tests/unittests"

    print setup_dir
    # use the default shared TestLoader instance
    test_loader = unittest.defaultTestLoader

    # use the basic test runner that outputs to sys.stderr
    test_runner = unittest.TextTestRunner()

    # automatically discover all tests
    # NOTE: only works for python 2.7 and later
    test_suite = test_loader.discover(setup_dir, pattern='unittest*.py')

    print test_suite

    # run the test suite
    test_runner.run(test_suite)

try:
    from setuptools.command.test import test

    class DiscoverTest(test):

        def finalize_options(self):
            test.finalize_options(self)
            self.test_args = []
            self.test_suite = True

        def run_tests(self):
            discover_and_run_tests()

except ImportError:
    from distutils.core import Command

    class DiscoverTest(Command):
        user_options = []

        def initialize_options(self):
                pass

        def finalize_options(self):
            pass

        def run(self):
            discover_and_run_tests()

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

  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
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