from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()
with open("requirements.txt", "r") as f:
    requirements = f.readlines()

setup(
    name="demo_package",
    version="0.0.1",
    author="Guilherme J. Araújo",
    author_email="guilherme.jose.ti@gmail.com",
    description="Some demonsration of python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="github.com/guilhermejra/demo_package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.6",
)