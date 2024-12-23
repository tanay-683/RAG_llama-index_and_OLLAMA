from setuptools import find_packages
from setuptools import setup

setup(
    name="rag_2",
    version="0.1",
    packages=find_packages(where="rag_2"),
    package_dir={"": "rag_2"},    
)