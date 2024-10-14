from setuptools import setup, find_packages

setup(
    name='flume',
    version='0.1.1',
    author="Flume",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.11",
    install_requires=[
        'pydantic',
        'httpx',
        'firebase-admin'
    ],
    entry_points={
        'console_scripts': [
        ],
    },
)
