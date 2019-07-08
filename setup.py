'''

Pip setup via setuptools

Copied mostly from:
https://dzone.com/articles/executable-package-pip-install

'''
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="terrabl",
    version="0.0.0",
    scripts=["terrabl"],
    author="Terrabl",
    author_email="alex+pip@iulius.io",
    description="Terrabl Terraform Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://terrabl.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix"
    ]
)