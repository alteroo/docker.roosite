################################
#  
#  run this script using
#  bin/instance -OPlone run {scriptname}
#  assumptions:
#   we assume that you have a working zope server with an instance
#   of plone located at the root named "Plone"
#   we also assume that you have an image named "
#
##################################################
from plone import api
import transaction

from AccessControl.SecurityManagement import newSecurityManager
from AccessControl.SecurityManager import setSecurityPolicy
from Testing.makerequest import makerequest
from Products.CMFCore.tests.base.security import PermissiveSecurityPolicy, OmnipotentUser

def spoofRequest(app):
    """
    Make REQUEST variable to be available on the Zope application server.
    This allows acquisition to work properly
    """
    _policy=PermissiveSecurityPolicy()
    _oldpolicy=setSecurityPolicy(_policy)
    newSecurityManager(None, OmnipotentUser().__of__(app.acl_users))
    return makerequest(app)

# Enable Faux HTTP request object so we can do "browsery" things on the cmd
app = spoofRequest(app)
request = app.REQUEST

# -------------------------
# -------------------------
#site = app['Plone']
# print site.Title()

api.portal.get()
portal = api.portal.get()
discount_partners = portal.membership['discount-partners']
folders = api.content.find(
    context=discount_partners,
    depth=1, 
    portal_type='Folder')

if len(folders) < 1:
    print("-----> Nothing to convert")
for folder in folders:
    # import ipdb;ipdb.set_trace()
    folder = folder.getObject()
    title,description,image = folder.title,folder.description,folder.image
    api.content.delete(obj=folder)
    print("---------> ",title)
    obj = api.content.create(
          type='category',
          title=title,
          description=description,
          container=discount_partners
              )
    obj.image = image

transaction.commit()