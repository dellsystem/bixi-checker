from distutils.core import setup


setup(
    name='Bixi API Wrapper',
    version='0.0.1',
    scripts='bin/bixi',
    packages='bixiapi',
    author='Wendy Liu',
    author_email='ilostwaldo@gmail.com',
    description="A simple wrapper for the bixi.com API. Well, there isn't \
                 actually an API, but you can pretend there is one if you \
                 use this module."
)
