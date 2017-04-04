
# -*- coding: utf-8 -*-

# The setuptools script to build, install and test a PyGeodesy distribution.

# Tested with 64-bit Python 2.7.13 and 3.6.0 (using setuptools 28.8.0) but
# on macOS 10.12.3 Sierra only.

# python setup.py sdist --formats=gztar,bztar,zip
#[python setup.py bdist_wheel --universal  # XXX]
# python setup.py test
# python setup.py install

# <https://packaging.python.org/key_projects/#setuptools>
# <https://packaging.python.org/distributing/>
# <https://docs.python.org/2/distutils/sourcedist.html>
# <https://docs.python.org/3.6/distutils/sourcedist.html>
# <https://setuptools.readthedocs.io/en/latest/setuptools.html#developer-s-guide>
# <https://setuptools.readthedocs.io/en/latest/setuptools.html#test-build-package-and-run-a-unittest-suite>
# <http://zetcode.com/articles/packageinpython/>

from setuptools import setup

__version__ = '17.03.10'


def _version():
    with open('geodesy/__init__.py') as f:
        for t in f.readlines():
            if t.startswith('__version__'):
                v = t.split('=')[-1].strip().strip("'").strip('"')
                return '.'.join(map(str, map(int, v.split('.'))))


def _long_description():
    with open('README.rst', 'rb') as f:
        t = f.read()
        if isinstance(t, bytes):
            t = t.decode('utf-8')
        return t


setup(
    name='PyGeodesy',
    packages=['geodesy', 'tests'],
    description='Python geodesy tools',
    version=_version(),

    author='Jean M. Brouwers',
    author_email='mrJean1 at Gmail dot com',
    maintainer='Jean M. Brouwers',
    maintainer_email='mrJean1 at Gmail dot com',

    license='MIT',
    keywords='geodesy datum development earth ellipsoid Lambert MGRS Nvector OSGR sphere trigonometry UTM Vincenty',
    url='https://github.com/mrJean1/PyGeodesy',

    long_description=_long_description(),

    package_data={'geodesy': ['LICENSE']},  # data_files=[]

    test_suite='tests.TestSuite',

    zip_safe=False,
    classifiers=[
        'Development Status ::  5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering :: GIS',
    ],

#   download_url='https://github.com/mrJean1/PyGeodesy',
#   entry_points={},
#   include_package_data=False,
#   install_requires=[],
#   namespace_packages=[],
#   py_modules=[],
)