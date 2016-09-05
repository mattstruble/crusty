from os.path import dirname, join
from setuptools import setup, find_packages

with open(join(dirname(__file__), 'crusty/VERSION'), 'rb') as f:
    version = f.read().decode('ascii').strip()

setup(
    name='Crusty',
    version=version,
    url='http://google.com',
    description='A game engine for creating terminal games',
    long_description=open('README.rst').read(),
    author='Matt Struble',
    maintainer='Matt Struble',
    maintainer_email='matt@mattstruble.com',
    license='MIT',
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['crusty = crusty.main:execute']
    },
    classifiers=[
        'Framework :: Crusty',
        'Development Status :: 0 - Prototype',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python 2',
        'Programming Language :: Python 2.7',
        'Topic :: Games :: Engine'
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
    
    
