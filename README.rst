.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
ccrp.site
==============================================================================

The following documentation is written for persons who will checkout and use this
package for development and deployment of the
ccrp project. If you want to generate a package like this
for a new project then take a look at
https://github.com/alteroo/roosite.launchkit

Thank you (or the developer that you're working with) for using our system.
If you are happy with the setup, reach out and let us know.

If you have found that there is need for improvement you are encouraged to contribute to the
project. Either by reporting bugs or contributing updates.

This package represents over a decade of experience working with Plone.
The goal is to make it as easy as possible to build a feature rich and secure Plone based CMS site.
The notes below provide guidelines for customizing the package to your needs.
The repository for this package is located
at http://gitlab.com/roo-ccrp/ccrp.site

Before you Start
================

Having the following in place will absolutely simplify your experience.

* Ensure you're doing development on an Ubuntu or Debian based machine (virtual or real). We now have experimental support for OS X also
  so you could get away with that.
* The user that executes the scripts should have sudo privileges (DON'T USE THE ROOT USER)

Compatibility
-------------
It is expected that you will be doing development on an Ubuntu Linux, Debian or OS X (experimental) system.
This has been tested on a crouton based Ubuntu 14.04 on ChromeOS, on
Cloud9 IDE and OS X.
This will not work on Fedora or Centos because
some scripts rely on the apt-get package manager (or homebrew on OS X).
It has not been thoroughly
tested on Debian but should work on the latest stable releases.

For development you should ideally have about 1GB of RAM however
we've done a few tricks to support machines with less RAM, we don't recommend
that you venture below 512MB if you value your sanity and productivity.

Development Quickstart - Method 1
=====================================

Bootstrap then bin buildout::

    virtualenv venv
    venv/bin/python bootstrap-buildout.py
    bin/buildout -c develop.cfg


Development Quickstart - Method 2
=====================================

Follow these steps to get going with development.

Step 1 - Clone the repository and change directory to checkout directory
-------------------------------------------------------------------------------
::

    git clone git@gitlab.com:roo-ccrp/ccrp.site.git
    cd ccrp.site

Step 2 - Prime the machine and install
--------------------------------------------
The following commands should be run from within the buildout directory::

    bash prime.sh
    bash install.sh

Step 3 - Then switch to development mode
-------------------------------------------------------------------------------
Do this with a symlink of buildout.cfg to the develop.cfg::

    ln -sf develop.cfg buildout.cfg
    bin/buildout -c develop.cfg

Importing data from the CCRP Plone 4.3.1 site
=================================================

Run the following command::

    ./installJsonData.sh Plone

What's inside
=============

.cfg files
----------

The .cfg files manage the characteristics of the site environment.
They make it possible for us to automate complex interactions
in a predictable and configurable manner.

The ``develop.cfg`` is the one used for setting up a
development environment and is enabled by default.

The ``production.cfg`` is used for deploying production environments.
These files are discussed in more detail below.

Old school Plone developers may notice that there is no ``buildout.cfg``.
This is not an accide`nt, the recommended approach is that you symlink to the
``develop.cfg`` when doing development file during development
and to the ``production.cfg`` when deploying to production.

Apart from these files, we also include the following supporting files:

- base.cfg
- haproxy.cfg
- ports.cfg
- rsync.cfg
- supervisord.cfg
- travis.cfg
- zeo.cfg

Manage packages and dependencies in setup.py
--------------------------------------------

If you need to make add-ons (some systems call these modules) and other supporting
packages available to your site, then you need to become familiar with `setup.py`.

The `setup.py`, located at
`src/ccrp/site/setup.py`, declares a list
of dependencies for the project. These dependencies are resolved whenever
a build is initiated. By default, dependencies
are pulled from the pypi repository (https://pypi.org/).

This package ships with the following dependencies:
::

        'plone.api',
        'plone.app.mosaic'
        'rapido.plone',
        'gloss.theme',
        'collective.documentviewer',
        'collective.routes',
        'collective.z3cform.norobots',
        'wildcard.media',
        'Products.GenericSetup>=1.8.2',
        'Products.PloneFormGen',
        'setuptools',
        'z3c.jbot',

These packages allow us to deliver a richer out of the box experience for
our customers.

Old school Plone developers may be used to managing dependencies and packages
in the buildout.cfg file. We consider that approach to be less straightforward
and not helpful when working with new developers.


Quickly sharing Datafiles
=========================
There is a pack and unpack script for quick sharing of data between developers.
To create a packed data distribution run the following command::

    bash packitup.sh

    This will create a `packeddb.tgz` file in your buildout folder.
    Give this to a fellow developer.

    To use a `packeddb.tgz` file place it in your buildout folder and run::

        bash unpackit.sh

Synchronizing Data with rsync.cfg
=================================
During development is it often useful to work on real data.

.. warning:: ALWAYS pull data from production, under NO circumstance should data be travelling from a development machine to a production machine.

Before you start
----------------

1. Edit ``rsync.cfg`` to point at the correct server
2. Make sure that your dev user account have shared keys with the production server

To synchronize data from the production server use the following command::

    bin/buildout -c rsync.cfg


Oneliner to sync and set admin password to admin::

    bin/buildout -c rsync.cfg && sh scripts/adminForDev.sh

Then start your dev server as normal

    bin/instance fg

Production Setup
================
To deploy to production you can run the following commands
From a user on the production server
::

    git clone git@gitlab.com:roo-ccrp/ccrp.site.git
    cd ccrp.site

Configuration
-------------
Edit ports.cfg to ensure there are no clashes with existing services

You'll need sudo privileges for this step::

    bash prime.sh

Finally install the production site::

    bash install-production.sh


Upcoming features
=================
Planned features and fixes are documented as issues at

https://github.com/alteroo/roosite.launchkit/issues


Initiating submodules without buildout
========================================

When cloning the repository, you may need to pull in the theme by running the
following code::

    git submodule update --init 
