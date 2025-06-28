from setuptools import setup, find_packages

setup(
    name="my_math",# package name
    version="v0.0.1",
    author="Fuad",
    author_email="fuad094@gmail.com",
    description="believe me ,its very interesting and useful",
    packages=find_packages(include=["mymath", "mymath.*"]),
    install_requires=[],

)