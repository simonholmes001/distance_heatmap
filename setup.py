from distutils.core import setup, Extension
import distutils.command.bdist_conda

setup(
    name="distance heatmap",
    version="0.0.1",
    distclass=distutils.command.bdist_conda.CondaDistribution,
    conda_buildnum=1,
    conda_features=['mkl'],
    conda_buildstr=py34_0,
    conda_import_tests=False,
    conda_command_tests=False,
)