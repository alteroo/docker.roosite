# Create a Plone site. This is a "run" script.

from Products.CMFPlone.factory import _DEFAULT_PROFILE
from Products.CMFCore.utils import getToolByName
from zope.component import getMultiAdapter
from Acquisition import aq_inner
from AccessControl.SecurityManagement import newSecurityManager
from AccessControl.SecurityManager import setSecurityPolicy
from plone import api
from Testing.makerequest import makerequest
from Products.CMFCore.tests.base.security import PermissiveSecurityPolicy, OmnipotentUser
from zope.component.hooks import setSite

import string
import random
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

import sys
import transaction

site_id = sys.argv[3]

if site_id in app.objectIds():
    print "Found Plone site named %s" % site_id
else:
    print "No site found"
    sys.exit(1)

# Sets the current site as the active site
setSite(app[site_id])
site = app[site_id]

manage_addProduct = site.manage_addProduct

em = manage_addProduct['ExternalMethod']
manage_addExternalMethod = em.manage_addExternalMethod
manage_addExternalMethod('get_item', 'get_item', 'collective.jsonify.json_methods', 'get_item')
manage_addExternalMethod('get_children', 'get_children', 'collective.jsonify.json_methods', 'get_children')
manage_addExternalMethod('get_catalog_results', 'get_catalog_results', 'collective.jsonify.json_methods', 'get_catalog_results')
manage_addExternalMethod('export_content', 'export_content', 'collective.jsonify.json_methods', 'export_content')

transaction.commit()
