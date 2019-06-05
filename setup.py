from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Package for managing dataset features',
    long_description=readme,
    author='Robert Kelly',
    author_email='robert.l.kelly3@gmail.com',
    url='https://github.com/rlkelly/dendrite',
    license=license,
    packages=find_packages(exclude=('examples'))
)
