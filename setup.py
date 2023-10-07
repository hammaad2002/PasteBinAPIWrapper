from setuptools import setup, find_packages
import sys

# Define the required packages based on Python version
python_requires = '>=3.5'  # 'typing' is not needed for Python 3.5 and above
install_requires = ['requests']

with open('README.md', 'r', encoding= 'utf-8') as fh:
    long_description = fh.read()

if sys.version_info < (3, 5):
    install_requires.append('typing')

setup(
    name='PasteBinAPIWrapper',
    version='0.0.1',
    author = 'Hammad Ali Khan',
    author_email= 'hammadalikhan2002@gmail.com',
    description= 'A simple working PasteBin API.',
    long_description= long_description,
    long_description_content_type='text/markdown',
    url = 'https://github.com/hammaad2002/PasteBinAPIWrapper',
    project_urls = {
        "Bug Tracker": "https://github.com/hammaad2002/PasteBinAPIWrapper/issues",
        "Repository": "https://github.com/hammaad2002/PasteBinAPIWrapper"
    }
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=install_requires,
    python_requires=python_requires,
)