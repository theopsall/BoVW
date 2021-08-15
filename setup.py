import os

from setuptools import setup


def read(fname):
    try:
        with open(os.path.join(os.path.dirname(__file__), fname)) as fh:
            return fh.read()
    except IOError:
        return ''


requirements = read('requirements.txt').splitlines()

setup(name='BoVW',
      version='0.0.1',
      description='Bag of Visual Words',
      url='https://github.com/theopsall/BoVW',
      author='Theodoros Psallidas',
      author_email='theopsall@gmail.com',
      license='MIT License',
      packages=['BoVW'],
      zip_safe=False,
      install_requires=requirements
      )
