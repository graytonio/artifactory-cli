from setuptools import setup

setup (
    name = "jfrog",
    version = "0.0.1",
    packages = ['jfrog'],
    entry_points = {
        'console_scripts': [
            'jf = jfrog.cli:entry_point'
        ]
    }
)