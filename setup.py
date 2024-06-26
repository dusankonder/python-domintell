from setuptools import setup

with open('README.md') as file:
    long_description = file.read()

setup(name='python-domintell',
      version='0.0.18',
      url='https://github.com/dusan.konder/python-domintell',
      license='MIT',
      author='Zilvinas Binisevicius',
      install_requires=["pyserial"],
      author_email='-',
      description="Python Library for the Domintell protocol",
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=['domintell', 'domintell.utils', 'domintell.connections', 'domintell.messages', 'domintell.modules'],
      platforms='any',
     )
