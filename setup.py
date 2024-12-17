from setuptools import setup, find_packages

setup(
    name='radgraph',
    version='0.1.13',
    author='Jean-Benoit Delbrouck',
    license='MIT',
    url='https://github.com/Stanford-AIMI/radgraph',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
    ],
    python_requires='>=3.8',
    install_requires=[
        'torch>=2.3.0',
        'transformers>=4.39.0',
        "appdirs",
        'jsonpickle',
        'filelock',
        'h5py',
        'spacy',
        'nltk',
        'dotmap',
        'pytest',
    ],
    packages=find_packages(),
    zip_safe=False)
