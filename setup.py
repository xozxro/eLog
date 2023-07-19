from setuptools import setup, find_packages
import subprocess
import sys
import os

def system_setup():
    setup(
        name='eLog',
        version='0.1',
        packages=find_packages(),
        entry_points={
            'console_scripts': [
                'elog = eLog:main',
            ],
            'eLog': [
                'eLog = eLog.elog:eLog',
            ]
        },

        install_requires=[
            'requests',
            'python-dateutil',
            'pytz',
        ],
    )

if __name__ == '__main__': system_setup()
