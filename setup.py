from setuptools import setup

setup(
    name='Cliweather',
    version='0.1.0',
    install_requires=[
        'Click',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'cliw=main.py:main',
        ],
    },
)
