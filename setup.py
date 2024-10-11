from setuptools import setup, find_packages

setup(
    name='radgraph',
    version='0.1.9',
    author='Jean-Benoit Delbrouck',
    license='MIT',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
    ],
    python_requires='>=3.8,<3.9',
    install_requires=['torch==2.2.1',
                      'transformers==4.39.0',
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
