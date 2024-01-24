from setuptools import setup, find_packages

setup(
    name='pyktc',
    version='0.1',
    description='A Python implementation of a basic keyword transposition cipher',
    author='w4ffl35',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pyktc = main:main',
        ],
    },
)