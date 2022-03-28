from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="uwuipy",
    version="0.0.3",
    description='A python library that "uwuifies" a given string',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_dir={'': "uwuipy"},
    url="https://github.com/SlumberDemon/uwuipy",
    author="SlumberDemon",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ]
)
