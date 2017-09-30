import sys
from setuptools import setup
exec(open('soilpy/version.py').read())

if sys.version_info[0] < 3 and sys.version_info[1] < 5:
    sys.exit('Sorry, python < 3.5 is not supported')

if __name__ == '__main__':
    setup(
        name='SoilPy',
        version=__version__,
        description='soilpy package',
        author='Rik Hendriks',
        author_email='rikhendriks@rocketmail.com',
        license='MIT License',
        packages=['soilpy', 'soilpy.core', 'soil.core.soil', 'soilpy.tests'],
        install_requires=[
            "numpy",
            "matplotlib"
        ]
    )