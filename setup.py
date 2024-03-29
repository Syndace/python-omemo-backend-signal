# pylint: disable=exec-used
import os
from typing import Dict, Union, List

from setuptools import setup, find_packages # type: ignore[import]

source_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "omemo_backend_signal")

version_scope: Dict[str, Dict[str, str]] = {}
with open(os.path.join(source_root, "version.py")) as f:
    exec(f.read(), version_scope)
version = version_scope["__version__"]

project_scope: Dict[str, Dict[str, Union[str, List[str]]]] = {}
with open(os.path.join(source_root, "project.py")) as f:
    exec(f.read(), project_scope)
project = project_scope["project"]

with open("README.md") as f:
    long_description = f.read()

classifiers = [
    "Intended Audience :: Developers",

    "License :: OSI Approved :: MIT License",

    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",

    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",

    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy"
]

classifiers.extend(project["categories"])

if version["tag"] == "alpha":
    classifiers.append("Development Status :: 3 - Alpha")

if version["tag"] == "beta":
    classifiers.append("Development Status :: 4 - Beta")

if version["tag"] == "stable":
    classifiers.append("Development Status :: 5 - Production/Stable")

del project["categories"]
del project["year"]

setup(
    version = version["short"],
    long_description = long_description,
    long_description_content_type = "text/markdown",
    license = "GPLv3",
    packages = find_packages(),
    install_requires = [
        "X3DH>=0.5.9,<0.6",
        "DoubleRatchet>=0.7.0,<0.8",
        "OMEMO>=0.13.0,<0.15",
        "cryptography>=3.3.2",
        "protobuf>=2.6.1"
    ],
    python_requires = ">=3.6,<4",
    include_package_data = True,
    zip_safe = False,
    classifiers = classifiers,
    **project
)
