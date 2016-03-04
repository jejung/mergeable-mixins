import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
        README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='mergeable_mixins',
    version='0.1',
    packages=['mergeable_mixins'],
    include_package_data=True,
    license='GNU 3.0 License',
    description='Adds support to use of mixins in models or other types of \
classes',
    long_description=README,
    url='https://github.com/jejung/mergeable_mixins',
    author='Jean Jung',
    author_email='jean.jung@rocketmail.com',
    classifiers=[
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License',
        'Operating System :: OS Independent',
        'Programming Language :: Python', 
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
    ],
)
