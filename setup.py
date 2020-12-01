# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='dolark',
    version='0.0.1',
    description='Dolo meets ARK',
    python_requires='==3.*,>=3.7.0',
    author='Winant Pablo',
    author_email='pablo.winant@gmail.com',
    license='BSD-2-Clause',
    packages=['dolark'],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        'altair==4.*,>=4.1.0', 'ipython==7.*,>=7.17.0',
        'jupyterlab==2.*,>=2.2.6', 'numpy==1.*,>=1.19.1',
        'ruamel.yaml==0.*,>=0.16.10', 'scipy==1.*,>=1.5.2', 'tqdm==4.*,>=4.48.2'
    ],
    extras_require={
        "dev": [
            "black==20.*,>=20.8.0.b1", "flake8==3.*,>=3.8.4",
            "mkdocs==1.*,>=1.1.0", "mypy==0.*,>=0.782.0",
            "pymdown-extensions==7.*,>=7.1.0", "pytest==5.*,>=5.2.0",
            "python-markdown-math==0.*,>=0.6.0"
        ]
    },
)
