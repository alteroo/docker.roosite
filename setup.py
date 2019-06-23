# -*- coding: utf-8 -*-
"""Installer for the ccrp.site package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='ccrp.site',
    version='1.0.1',
    description="The Caribbean Community of Retired Persons (CCRP) is a non-profit membership organization for persons 50 and over, retired or preparing for retirement.",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.1-pending",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='Oshane Bailey',
    author_email='b4.oshany@gmail.com',
    url='https://pypi.python.org/pypi/ccrp.site',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['ccrp'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.app.mosaic',
        'collective.easyform',
        'collective.collectionfilter',
        'collective.documentviewer',
        'collective.routes',
        'collective.themesitesetup',
        'collective.z3cform.norobots',
        'gloss.theme',
        'plone.api',
        'plone.app.theming',
        'plone.app.themingplugins',
        'plone.restapi',
        'Products.GenericSetup>=1.8.2',
        'Products.PloneFormGen',
        'Products.QuickImporter',
        'rapido.plone',
        'setuptools',
        'wildcard.media',
        'webcouturier.dropdownmenu',
        'z3c.jbot',

    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
