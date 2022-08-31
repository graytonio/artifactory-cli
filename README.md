# artifactory-cli

A CLI for interacting with JFrog APIs

## Installation

The CLI can be installed from the repository by cloning and then running

```bash
./install.sh
```

The CLI can also be installed from the JFrog Repository if you have access to it using

```bash
pip3 install jfrog
```

## CLI Structure

The cli is broken up into individual modules for each sub command this allows easy expansion in the future to extend to other apis in the future. Common functions like interacting with the config file or making HTTP requests are stored in the top level module for use in all submodules.

#### Auth

This modules contains all the commands used to setup authentication with JFrog APIs. Currently it only contains a function to set the user and access token used for authenticating.

#### Artifactory

This module contains all the commands relating to the Artifactory API.

## Resources Used For Building This Project

- [Project Boilerplate](https://trstringer.com/easy-and-nice-python-cli/#funcmodulepy)
- [API Reference](https://www.jfrog.com/confluence/display/JFROG/Artifactory+REST+API)
- [CLI Library](https://click.palletsprojects.com/en/8.1.x/)
