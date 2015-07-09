try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'mahnobPlayer is a mediaplayer designed for the "Mahnob-db hci-tagging" database (http://mahnob-db.eu/hci-tagging/)',
    'author': 'Simone Castellani',
    'url': 'https://bitbucket.org/sfrullo/mahnobplayer',
    'download_url': 'https://bitbucket.org/sfrullo/mahnobplayer',
    'author_email': 'mail@simonecastellani.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['mahnobplayer'],
    'scripts': [],
    'name': 'mahnobplayer'
}

setup(**config)