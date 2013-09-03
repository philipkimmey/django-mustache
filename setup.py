from setuptools import setup
from setuptools import find_packages

setup(
    name="django-mustache",
    version="0.1",
    author="Philip Kimmey",
    author_email="philip.kimmey@gmail.com",
    description="Basic mustache support in Django templates",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Framework :: Django",
    ],
    install_requires=[
        "pystache>=0.5.3"
    ],
    packages=find_packages(),
    package_dir={'django_mustache': 'django_mustache'},
)
