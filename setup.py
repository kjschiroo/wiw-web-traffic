from setuptools import setup

setup(
    name='webtraffic',
    version='0.1',
    description='A single machine script for tranforming web traffic logs',

    author='Kevin Schiroo',
    author_email='kjschiroo@gmail.com',

    packages=['webtraffic'],
    entry_points = {
        'console_scripts': ['wttransform=webtraffic.cmdline:main'],
    },
    install_requires=[
        'docopt', 'requests'
    ]
)
