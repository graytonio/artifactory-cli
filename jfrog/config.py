import configparser
from pathlib import Path

_config_file = Path.joinpath(Path.home(), ".jfcfg")
_config = configparser.ConfigParser()

def get_config(section: str, key: str):
    _config.read(_config_file)
    if not section in _config:
        return None
    if not key in _config[section]:
        return None
    return _config[section][key]

def set_config(section: str, key: str, value: str):
    _config.read(_config_file)
    if not section in _config:
        _config[section] = {}
    _config[section][key] = str(value)
    with open(_config_file, 'w') as configfile:
        _config.write(configfile)