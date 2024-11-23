from setuptools import find_packages, setup
from typing import List


HYPEN_DOT = "-e ."


def get_install_required(file_name: str) -> List[str]:
    requirements = []
    with open(file_name) as file_object:
        requirements = file_object.readlines()
        requirements = [
            req.replace("\n", "") for req in requirements if req != HYPEN_DOT
        ]

    return requirements


setup(
    name="NLP Text Summarization",
    version="0.0.1",
    description="Model to do the text summarization.",
    author="Shivakumar Ravichandran",
    author_email="shivakumar.mcet@gmail.com",
    packages=find_packages(),
    install_requires=get_install_required("requirements.txt"),
)
