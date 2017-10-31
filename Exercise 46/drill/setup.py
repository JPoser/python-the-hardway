try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'drill project from Exercise 46',
	'author': 'JPoser',
	'url': 'https://github.com/JPoser/python-the-hardway/tree/master/Exercise%2046/drill',
	'download_url': 'https://github.com/JPoser/python-the-hardway/tree/master/Exercise%2046/drill',
	'author_email': 'My email.',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['drill'],
	'scripts': ['bin/script.py'],
	'name': 'python-drill'
}

setup(**config)