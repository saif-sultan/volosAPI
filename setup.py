"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from distutils.core import setup
setup(
  name = 'volosAPI',
  packages = ['volosAPI'],
  version = "1.6",
  license='MIT',
  description =  'Volos Portfolio Solutions LLC, Data API Python Integrator',
  author='Volos Portfolio Solutions',
  author_email='info@volossoftware.com',

  url = 'https://github.com/saif-sultan/volosAPI',
  download_url = 'https://github.com/saif-sultan/volosAPI/archive/v_16.tar.gz',
  keywords = ['Volos', 'Data API', 'FinTech'],
  install_requires=["pandas", "requests"],
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