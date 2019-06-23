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
import csv
from zope.component import getUtility
from plone.i18n.normalizer.interfaces import IIDNormalizer


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
filename = "scripts/partners.csv"


        
api.portal.get()
portal = api.portal.get()
discount_partners = portal.membership['discount-partners']

def create_discount_partner(data,container):
    d_partner = api.content.create(
              type='discount_partner',
              container=container,
              title=data['company'],
              phone1=data['phone1'],
              phone2=data['phone2'],
              phone3=data['phone3'],
              address=data['address'],
              fax=data['fax'],
              discount_description=data['discount description'],
              website=data['website'],
              facebook=data['facebook'],
              instagram=data['instagram'],
              twitter=data['twitter'],
              youtube=data['youtube']
              )

_n = getUtility(IIDNormalizer)


categories = discount_partners.objectIds()

# initializing the titles and rows list 
fields = [] 
rows = [] 
  
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = csvreader.next() 
  
    # extracting each data row one by one 
    for row in csvreader:
        data = dict(zip(fields, row))
        cat_title = data['category']
        if len(cat_title) > 3:
            cat_id = _n.normalize(cat_title)
            if cat_id in categories:
                cat_folder = discount_partners[cat_id]
            else:
                # create new category
                cat_folder = api.content.create(
                  type='category',
                  container=discount_partners,
                  title=cat_title
                  )
                categories.append(cat_id)
            create_discount_partner(data,cat_folder)
        

transaction.commit()