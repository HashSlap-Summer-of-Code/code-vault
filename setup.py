from setuptools import setup

setup(
    name='codevault',
    version='0.1.0',
    packages=['codevault'],
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={'console_scripts': ['codevault=codevault.cli:main']}
)