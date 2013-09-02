from setuptools import setup

setup(
    name="django-mustache",
    version="0.1",
    author="Philip Kimmey",
    author_email="philip.kimmey@gmail.com",
    description="Basic mustache support in Django templates",
    license="MIT",
    platforms=["Any"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Framework :: Django",
    ],
    install_requires=[
        "pystache>=0.5.3"
    ],
    packages=['django_mustache'],
    package_dir={'django_mustache': 'django_mustache'},
    include_package_data=True,
    package_data={
        'django_mustache': [
            '*.py',
            'template/*.py',
            'template/loaders/*.py',
            'tests/*.py']
    }
)
