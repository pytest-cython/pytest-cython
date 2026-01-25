#!/usr/bin/env python
# -*- encoding: utf-8 -*-


if __name__ == "__main__":
    import sys

    from setuptools import setup
    from setuptools import Extension
    from Cython.Build import cythonize

    directives = {
        'autotestdict': True,
        'embedsignature': False,
        'language_level': sys.version_info[0],
        'linetrace': False,
        'profile': False,
    }

    extensions = [
        Extension('*', ['src/pypackage/*.pyx'])
    ]

    setup(
        name='pytest-cython-example',
        version='0.3.1',
        description="Example Cython project for pytest-cython tests",
        package_dir={'': 'src'},
        packages=['pypackage'],
        zip_safe=False,
        ext_modules=cythonize(extensions, compiler_directives=directives)
    )
