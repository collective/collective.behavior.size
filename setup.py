from setuptools import find_packages
from setuptools import setup

import os


long_description = (
    open(os.path.join("collective", "behavior", "size", "docs", "README.rst")).read() + "\n" +
    open(os.path.join("collective", "behavior", "size", "docs", "HISTORY.rst")).read() + "\n" +
    open(os.path.join("collective", "behavior", "size", "docs", "CONTRIBUTORS.rst")).read())


setup(
    name='collective.behavior.size',
    version='0.2.1',
    description="Provides size related behavior, such as weight and three dimensional size, to dexterity content types.",
    long_description=long_description,
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@gmail.com',
    url='https://github.com/collective/collective.behavior.size/',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.behavior'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Plone>=4.2',
        'five.grok',
        'hexagonit.testing',
        'plone.behavior',
        'setuptools',
        'zope.i18nmessageid'],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
