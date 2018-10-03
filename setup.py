from setuptools import setup, find_packages
import os


def lines(path):
    with open(path) as f:
        return f.readlines()


win32_req = lines("win32.requirements.txt")
linux_req = lines("linux.requirements.txt")
all_req = lines("requirements.txt")

requirements = [*all_req, *(win32_req if os.name == "nt" else linux_req)]

setup(
    name="toast",
    description="A cross platform python library for toast notifications",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements
)
