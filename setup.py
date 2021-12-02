from setuptools import find_packages, setup
from distutils.util import convert_path

version_path = convert_path('server/npg/version.py')
namespace = {}
with open(version_path) as ver_file:
    exec(ver_file.read(), namespace)

setup(
    name='npg-porch',
    version=namespace['__version__'],
    package_dir={
        'npg': './server'
    },
    packages=['npg'],
    license='Apache License 2.0',
    author='Wellcome Sanger Institute',
    author_email='npg@sanger.ac.uk',
    description='Work allocation and tracking for portable pipelines',
    install_requires=[
        'aiosqlite',
        'asyncpg',
        'fastapi',
        'pydantic',
        'psycopg2-binary',
        'sqlalchemy',
        'ujson',
        'uvicorn'
    ]
)