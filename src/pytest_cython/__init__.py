from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("pytest-cython")
except PackageNotFoundError:
    import warnings
    warnings.warn('could not get pytest-cython version')
    __version__ = '0.0.0'
