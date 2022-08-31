from setuptools import setup

setup (
    name = "jfrog",
    description= "JFrog Interview Assignment",
    author = "Grayton Ward",
    author_email= "graytonio.ward@gmail.com",
    version = "0.0.1",
    packages = ['jfrog', 'artifactory', 'auth'],
    entry_points = {
        'console_scripts': [
            'jf = jfrog.cli:entry_point'
        ]
    }
)