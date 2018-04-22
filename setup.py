from setuptools import setup

setup(
    name='build-pulse-project',
    packages=['build-pulse-project'],
    include_package_data=True,
    install_requires=[
        'flask',
        'jsonschema'
    ],
)
