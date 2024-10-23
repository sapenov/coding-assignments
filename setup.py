
from setuptools import setup, find_packages

setup(
    name="beyond_bets",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pyspark==3.2.1",
        "pytest==7.1.2",
        "flake8==5.0.4",
        "black==22.3.0",
    ],
    extras_require={
        "dev": ["pytest", "flake8", "black"]
    },
)
