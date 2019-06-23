# Create a Plone site. This is a "run" script.
import sys
import transaction
from Products.CMFPlone.factory import _DEFAULT_PROFILE
from Products.CMFPlone.factory import addPloneSite
from plone import api
from zope.component.hooks import setSite
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.interfaces import INavigationSchema
from Products.CMFPlone.interfaces.controlpanel import IImagingSchema
from Products.CMFPlone.interfaces.controlpanel import ISiteSchema
from zope.component import getUtility

site_id = sys.argv[3]
SITE_TITLE = u"CCRP"

#language = "en-jm"
default_extension_profiles = (
    'plone.app.caching:default',
    'plonetheme.barceloneta:default',
    'ccrp.site:default'
)
print("----------> Initiating install of {} site".format(site_id))

if site_id in app.objectIds():
    print "The site was already installed"
    sys.exit(1)

site = addPloneSite(
    app, site_id,
    title=SITE_TITLE,
    profile_id=_DEFAULT_PROFILE,
    extension_ids=default_extension_profiles,
    setup_content=True,
#    default_language=language,
    )


# Sets the current site as the active site
print("----------> Setting {} as the active site".format(site_id))
setSite(app[site_id])
registry = getUtility(IRegistry)
navigation_settings = registry.forInterface(
    INavigationSchema,
    prefix='plone'
)
image_settings = registry.forInterface(
    IImagingSchema,
    prefix='plone'
)
site_settings = registry.forInterface(
    ISiteSchema,
    prefix='plone'
)

# set up navigation settings
print("----------> Setting Navigation settings")
navigation_settings.nonfolderish_tabs = False
navigation_settings.workflow_states_to_show = ('published',)
navigation_settings.filter_on_workflow = True
navigation_settings.displayed_types = ('Event', 'File', 'Folder',
                                       'FormFolder', 'Image', 'Link',
                                       'News Item', 'Document')
print("----------> Setting Site settings")
site_settings.enable_sitemap = True
site_settings.site_title = SITE_TITLE

print("----------> Setting Custom Image settings")
image_settings.allowed_sizes = [
                                u'large 768:768', u'preview 400:400',
                                u'mini 200:200', u'thumb 128:128',
                                u'tile 64:64', u'icon 32:32',
                                u'listing 16:16', u'two_fifty 250:250',
                                u'custom 500:375']


transaction.commit()
