#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()


with open("requirements.txt") as reqs_file:
    requirements = reqs_file.read().strip().split("\n")


test_requirements = [
    "pytest>=3",
]

setup(
    author="Chris Havlin",
    author_email="chris.havlin@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="sandbox for testing dask, pytest CI config",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="ci_sandbox",
    name="ci_sandbox",
    packages=find_packages(include=["ci_sandbox", "ci_sandbox.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/chrishavlin/ci_sandbox",
    version="0.1.0",
    zip_safe=False,
)
