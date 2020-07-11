from setuptools import setup
from distutils.core import setup, Extension

setup(
    name='distance_heatmap',
    version='0.0.1',
    packages=['distance_heatmap'],
    url='https://github.com/simonholmes001/distance_heatmap',
    license='BSD',
    author='simon holmes',
    author_email='simon@mathisi.ai',
    description='Creates a distance heatmap from a distance or adjacency matrix',
    conda_buildnum=1,
)
