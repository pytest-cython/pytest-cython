#!/usr/bin/env python


if __name__ == "__main__":
    import sys

    from Cython.Build import cythonize
    from setuptools import Extension, setup

    directives = {
        "autotestdict": True,
        "embedsignature": False,
        "language_level": sys.version_info[0],
        "linetrace": False,
        "profile": False,
    }

    extensions = [Extension("*", ["src/pypackage/*.pyx"])]

    setup(
        name="pytest-cython-example",
        version="0.0.1",
        description="Example Cython project for pytest-cython tests",
        package_dir={"": "src"},
        packages=["pypackage"],
        zip_safe=False,
        ext_modules=cythonize(extensions, compiler_directives=directives),
    )
