from setuptools import setup, find_packages

setup(
    name='pyktc',
    version='1.0.0',
    author='w4ffl35',
    description='A Python implementation of a basic keyword transposition cipher',
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="cipher, keyword transposition cipher, ktc, transposition cipher",
    license='MIT',
    url="https://github.com/w4ffl35/pyktc",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    entry_points={
        'console_scripts': [
            'pyktc = pyktc.main:main',
        ],
    },
)