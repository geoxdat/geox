from geox.version import VERSION
from setuptools import setup
import pathlib


BASE_DIR = pathlib.Path(__file__).parent
README = (BASE_DIR / "README.md").read_text()

setup(
    name="geox",
    version=VERSION,
    author="GeoX",
    author_email="geoxdat@gmail.com",
    url='https://github.com/geoxdat/geox',
    description="GeoX, Geostatic Dataset Integration Tool",
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=[
        'geox', 
        'geox/api_caller',
        'geox/entity',
        'geox/factory',
        'geox/http_response',
        ],
    include_package_data=True,
    install_requires=[
        'numpy',
        'pandas',
        'pytest',
        'pytz',
        'requests',
        'tqdm',
        ],
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
