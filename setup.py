# -*- coding: utf-8 -*-
"""Installer for the incrementic.plonesite package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='incrementic.plonesite',
    version='1.0a1',
    description="Incrementic Website",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='David Bain',
    author_email='david@alteroo.com',
    url='https://github.com/collective/incrementic.plonesite',
    project_urls={
        'PyPI': 'https://pypi.python.org/pypi/incrementic.plonesite',
        'Source': 'https://github.com/collective/incrementic.plonesite',
        'Tracker': 'https://github.com/collective/incrementic.plonesite/issues',
        # 'Documentation': 'https://incrementic.plonesite.readthedocs.io/en/latest/',
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['incrementic'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires="==2.7",
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'collective.collectionfilter',
        'collective.documentviewer',
        'collective.easyform',
        'collective.routes',
        'collective.themefragments',
        'collective.themesitesetup',
        'collective.z3cform.norobots',
        'plone.app.mosaic',
        'rapido.plone',
        'wildcard.media',
        'webcouturier.dropdownmenu',
        'Products.GenericSetup>=1.8.2',
        'Products.PloneFormGen',
        'Products.QuickImporter',
        'z3c.jbot',
        'plone.api>=1.8.4',
        'plone.restapi',
        'plone.app.dexterity',
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
    [console_scripts]
    update_locale = incrementic.plonesite.locales.update:update_locale
    """,
)
