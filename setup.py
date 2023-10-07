from setuptools import setup, find_packages
import sys

# Define the required packages based on Python version
python_requires = '>=3.5'  # 'typing' is not needed for Python 3.5 and above
install_requires = ['requests']

if sys.version_info < (3, 5):
    install_requires.append('typing')

setup(
    name='pasteBinAPIWrapper',
    version='0.1',
    packages=find_packages(),
    install_requires=install_requires,
    python_requires=python_requires,
)