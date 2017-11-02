try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'ex48 course work',
	'author': 'JPoser',
	'url': 'https://github.com/JPoser/python-the-hardway',
	'download_url': 'Whttps://github.com/JPoser/python-the-hardway',
	'author_email': 'My email.',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex48'],
	'scripts': [],
	'name': 'ex48-lexicon'
}

setup(**config)