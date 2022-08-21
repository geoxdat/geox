from setuptools import setup
import pathlib

BASE_DIR = pathlib.Path(__file__).parent
README = (BASE_DIR / "README.md").read_text()

with open(f'{BASE_DIR}/requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="geox",
    version="0.0.1",
    author="GeoX",
    author_email="geoxdat@gmail.com",
    url='https://github.com/geoxdat/geox',
    description="GeoX, Geostatic Dataset Integration Tool",
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['geox'],
    include_package_data=True,
    install_requires=required,
    keywords=['geox', 'geostatistic', 'mining', 'dataset'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
