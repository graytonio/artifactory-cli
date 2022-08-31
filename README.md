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

## Authentication

Authentication is handled by access tokens that can be generated under the User Management section of the platform configuration and using that as the password for `jf auth login`. This was done to avoid recording a user password in plain text.

## .jfcfg

The CLI uses a configuration file in your home directory called `.jfcfg` this is where the settings for the base url, access token, and username are stored. Typically this file will not need to be edited manually instead being filled out by the `jf auth login` command.

## CLI Structure

The CLI is broken up into individual modules for each sub command this allows easy expansion in the future to extend to other apis in the future. Common functions like interacting with the config file or making HTTP requests are stored in the top level module for easy reuse in all submodules.

#### Auth

This modules contains all the commands used to setup authentication with JFrog APIs. Currently it only contains a function to set the user and access token used for authenticating.

#### Artifactory

This module contains all the commands relating to the Artifactory API.

## Future Plans

- [ ] Username/Password auth to generate long term access tokens
- [ ] More descriptive and helpful error messages
- [ ] Better coverage of API endpoints

## Resources Used For Building This Project

- [Project Boilerplate](https://trstringer.com/easy-and-nice-python-cli/#funcmodulepy)
- [API Reference](https://www.jfrog.com/confluence/display/JFROG/Artifactory+REST+API)
- [CLI Library](https://click.palletsprojects.com/en/8.1.x/)
