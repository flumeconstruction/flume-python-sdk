from setuptools import setup, find_packages

setup(
    name='flume',
    version='0.1.8',
    python_requires=">=3.11",
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
        ],
    },
)
