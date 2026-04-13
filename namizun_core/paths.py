import os
from os import path

_DEFAULT_HOME = '/var/www/namizun'


def get_namizun_home():
    """Directory containing uploader.py, else/, and data files. Override with NAMIZUN_HOME."""
    return path.abspath(os.environ.get('NAMIZUN_HOME', _DEFAULT_HOME))


def range_ips_path():
    return path.join(get_namizun_home(), 'range_ips')


def bundled_range_ips_path():
    return path.join(get_namizun_home(), 'else', 'range_ips')


def log_path():
    return path.join(get_namizun_home(), 'namizun.log')
