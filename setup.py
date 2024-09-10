from setuptools import setup, find_packages

setup(
    name='flume',
    version='0.0.1',
    author="Flume",
    package_dir={"": "src"},
    packages=find_packages(),
    python_requires=">=3.11",
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
        ],
    },
)
