from setuptools import setup

setup(
    name='build_pulse',
    packages=['build_pulse'],
    include_package_data=True,
    install_requires=[
        'flask',
        'jsonschema'
    ],
)
