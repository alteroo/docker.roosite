.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

=====================
incrementic.plonesite
=====================

Tell me what your product does

Features
--------

- Can be bullet points


Running with Docker
---------------------

::

   docker  run -it -v $(pwd)/resources/theme:/plone/instance/resources/theme  -p 8080:8080 alteroo/roosite

Place your theme in the resources/theme folder.


Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar


Translations
------------

This product has been translated into

- Klingon (thanks, K'Plai)


Installation
------------

Install incrementic.plonesite by adding it to your buildout::

    [buildout]

    ...

    eggs =
        incrementic.plonesite


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/incrementic.plonesite/issues
- Source Code: https://github.com/collective/incrementic.plonesite
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
