'''

Pip setup via setuptools

Copied mostly from:
https://dzone.com/articles/executable-package-pip-install

'''
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="terrabl",
    version="0.0.0",
    entry_points={
        'console_scripts':[
            'terrabl = Terrabl.main:main'
        ]
    },
    install_requires=required,
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
    ],
    include_package_data=True,
    data_files=[('requirements.txt')],
    zip_safe=False
)