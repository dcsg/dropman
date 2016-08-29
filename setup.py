"""Packaging settings."""

from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from dropman import __version__

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()


def read_requirements(filename):
    try:
        with open(filename) as f:
            return f.read().splitlines()
    except IOError:
        import os
        raise IOError(os.getcwd())


class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test', '--cov=dropman', '--cov-report=term-missing'])
        raise SystemExit(errno)


setup(
    name='dropman',
    version=__version__,
    description='A digital ocean management command line program in Python.',
    long_description=long_description,
    url='https://github.com/dcsg/dropman',
    author='Daniel Gomes',
    author_email='me@danielcsgomes.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='digitalocean droplet droplets',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=read_requirements('requirements.txt'),
    extras_require={
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points={
        'console_scripts': [
            'dropman=dropman.cli:main',
        ],
    },
    cmdclass={'test': RunTests},
)
