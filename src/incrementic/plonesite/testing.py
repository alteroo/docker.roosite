# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import incrementic.plonesite


class IncrementicPlonesiteLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=incrementic.plonesite)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'incrementic.plonesite:default')


INCREMENTIC_PLONESITE_FIXTURE = IncrementicPlonesiteLayer()


INCREMENTIC_PLONESITE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(INCREMENTIC_PLONESITE_FIXTURE,),
    name='IncrementicPlonesiteLayer:IntegrationTesting',
)


INCREMENTIC_PLONESITE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(INCREMENTIC_PLONESITE_FIXTURE,),
    name='IncrementicPlonesiteLayer:FunctionalTesting',
)


INCREMENTIC_PLONESITE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        INCREMENTIC_PLONESITE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='IncrementicPlonesiteLayer:AcceptanceTesting',
)
