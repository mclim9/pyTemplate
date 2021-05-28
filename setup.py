# ##############################################################################
# ## Reference: https://python-packaging.readthedocs.io/en/latest/minimal.html
# ##
# ## python setup.py register            #Reserve name in pypi
# ## python setup.py --help-commands     #Help
# ## python setup.py install             #Installs package
# ## python setup.py install_scripts
# ## pip install .                       #Installs package in directory
# ## pip install -e .                    #Install editable package
# ##############################################################################
# ## Upload to PyPi
# ## python setup.py sdist           #Creates <pkg>.tar.gz
# ## twine upload .\dist\covid-2020.06.02.tar.gz

# import os
from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='covid',
    version='2020.06.2',
    description='Covid code of the world',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: Freely Distributable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='covid ',
    url='https://github.com/mclim9/covid',
    author='Martin Lim',
    author_email='martin.lim@rsa.rohde-schwarz.com',
    license='R&S Terms and Conditions for Royalty-Free Products',
    packages=find_packages(exclude=['test', 'proto']),
    install_requires=[
        'pyvisa>=1.9.0',
        'future_fstrings>=1.0.0',
    ],
    test_suite='test',
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'covid=covid.bin.cli:main'
            ],
    },
)
