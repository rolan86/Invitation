try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

config ={
    'description': 'Invitation',
	'author_email': 'merryl.rolan@gmail.com',
	'version': '0.1',
	'install_requires': requirements,
	'packages': ['Invitation'],
	'scripts': [],
	'name': 'invitation'
}

setup(**config)