from setuptools import setup
import os, sys

setup(
  name='vectorizedMinHash',
  version='0.0.2',
  packages=['vectorizedMinHash'],
  keywords = ['minhash', 'cuda', 'simhash', 'lsh'],
  description='Vectorized minhashing',
  url='https://github.com/bradhackinen/vectorizedMinHash',
  author='Brad Hackinen',
  author_email='',
  license='MIT',
  install_requires=[
    'numpy==1.20.1',
  ],
  package_data={
    'vectorizedMinHash': ['*'],
  },
)