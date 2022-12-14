from setuptools import setup

setup(
    name='Random Cards',
    version='1.0.0',
    description='Random Card Json Generator',
    author='lilloukas',
    author_email='colejh@bu.edu',
    url='https://github.com/lilloukas/pytest',
    py_modules=['app'],
    install_requires=['chris_plugin'],
    license='MIT',
    entry_points={
        'console_scripts': [
            'commandname = app:main'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ],
    extras_require={
        'none': [],
        'dev': [
            'pytest~=7.1',
            'pytest-mock~=3.8'
        ]
    }
)
