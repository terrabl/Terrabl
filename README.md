# <img src="img/logo.png" height=30> Terrabl

Main Repo for Terrabl Terraform Tool 

## Website

* [Main Website](https://terrabl.com)

## Goals

* Make a NodeJS-based command line tool that builds cloud systems simply and integrates seamlessly into existing [Terraform](https://www.terraform.io/) frameworks.
* Make an accessible tool for developers to build and deploy cloud-based tools quickly without being concerned about complex architectural considerations or images. 

## Contributing

[Please Follow Contributing Guidelines](CONTRIBUTING.md)

## Install Terraform

[Install Instructions](https://askubuntu.com/questions/983351/how-to-install-terraform-in-ubuntu#answer-983352)

## Install Terrabl

```bash 
pip install terrabl
```

## Setup

```bash 
terrabl init [-s || --silent] [-l || --location=path/to/directory]
```

* Creates `terrabl.json` in local directory
* Fills in `terrabl.json` from questionnaire
* **-s || --silent**: do not use questionnaire (defaults only)
* **-l || --location**: use location specified rather than current directory

## terrabl.json Structure

_This happens **once** in a single terrabl project_

```js
{
    "name": "My App", // Your App's Name (to be used for naming resources)
    "AWS_config": {
        // TODO: Fill this
    },
    "GCP_config": {
        // TODO: Fill this
    },
    "azure_config": {
        // TODO: Fill this
    },
    "terrabl_config": {
        "terrablignore": "path/to/.terrablignore", // not needed if in same folder as terrabl.json
        "working_dir": "path/to/working_directory_base/", // not needed if base directory contains this terrabl.json
        "build_to": "path/to/build/directory/", // directory to which compiled/built code will be sent, if not included, it will be working directory
        "build_commands": [
            // Array of bash-style commands to be run as pre-deployment build commands from the build directory. If these fail, the apply will not be allowed
        ],
        "test_dir": "path/to/testing/directory/", // where unit tests are held, this will not be included in resources
        "test_commands": [
            // Array of bash-style commands to be run as tests from the testing directory, if these fail, the apply will not be allowed
        ]
    }
}
```

## t.json Structure

_Put this in any folder containing the base directory of a **single resource**_

```js
{
    "name": "MyResource", // name to be used in creation of resource
    "resouce_type": "aws/lambda", // resource type
    "ignore": [ // local ignores
        "path/to/ignored/folder/",
        "path/to/ignored.file",
        "path/to/**/ignored/glob/*.js"
    ],
    "options": { // Resource-specific options
        // TODO: Fill this
    }
}
```

## Test/Stage Changes

_Testing is important!!_ This step runs the tests and build processes defined in the `terrabl.json`

```bash
terrabl stage
```

## Apply Changes

Sends all changes to respective cloud services.

```bash 
terrabl apply
```