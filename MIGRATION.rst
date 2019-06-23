Migration
================

Content Export
--------------
Content export is made possible by collective.jsonify. In order to have a
greater level of flexibility over the exporter we have forked it and
added it as a source for our purposes.

Preparation
--------------
Make sure that you have the latest data before running the export

    bin/buildout install data data-blob

Custom Script
--------------------
We have a script (installJsonify.py) which installs some custom methods from collective.jsonify.
They are installed as ExternalMethods (this is an old but reliable way
of providing custom code to a Zope based site).

.. note:: The ExternalMethods are script called from collective.jsonify/src/collective/jsonify/Extensions

The methods are used to provide an export step for our migration. You can install them by running the following
from the buildout.
::

    bin/instance run scripts/installJsonify.py Plone

This assumes we're adding it to a site in the root of the zope application server named ``Plone``.

The following queries should now work::

    http://localhost:8080/Plone/front-page/get_item
    http://localhost:8080/Plone/front-page/get_children


Here is an example of a catalog query::

    curl --data catalog_query=$(echo '{"Type": "Slide"}' | base64 -w0) \
  'http://localhost:8080/Plone/portal_catalog/get_catalog_results


Doing an export
--------------------
To start the export start the instance::

    bin/instance fg

And call the 'export_content' method via the url in your browser:

http://localhost:8080/Plone/export_content

or run this command in a separate terminal (replace username and password appropriately)::

    curl -u username:password http://localhost:8080/Plone/export_content

The result will be a folder in the /tmp with a name similar to ``/tmp/content_Plone_2016-01-23-19-41-42/``
Drilling down into that folder will reveal a file structure like this::

    |_ 0 -
       |_ *.json


A oneliner to list all the different types of content exported
-----------------------------------------------------------------
The following script will output the types of content stored in the JSON files (replace with the path
to your exported content)::

   grep "\"_type\"" content/*.json  | cut -d : -f 2,3 | uniq

Based on this we can start to determine which types we want to import from json and which can be moved with some other method.

Moving the exported content to the target buildout
--------------------------------------------------------

Move the exported folder to
`ccrp.site/content`
of `ccrp.site` buildout

You could achieve this with the following command from the ccrp.site buildout::

   mv /tmp/content_Plone_XXXXXXX ccrp.site/content

replace XXXXX with the correct strings to match your export.


Further Reading
--------------------
For more information see the documentation on collective.jsonify at https://collectivejsonify.readthedocs.org/

