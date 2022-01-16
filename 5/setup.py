
from setuptools import setup, find_packages

setup(
    name="src",
    version="1.0.0",
    description="apply a consistent format to `setup.cfg` files",
    long_description="file: README.md",
    author="Maciej Rybacki",
    author_email="rybackimaciej03@gmail.com",
    packages=find_packages(),
    url="https://github.com/Levarix/TAU_2021",
    setup_requires=["pytest-runner==5.3.1"],
    tests_require=["pytest==6.2.5", "pytest-cov==3.0.0"],
    extras_require={
        "testing": [
            "pytest-xdist",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.9"
    ],
)