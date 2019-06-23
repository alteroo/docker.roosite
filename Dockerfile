FROM plone:5

RUN apt-get update && apt-get install --no-install-recommends  git python-dev build-essential -y

ENV PACKAGENAME=incrementic.plonesite
COPY --chown=plone:plone . /plone/instance/src/$PACKAGENAME

# add your dependent files here
COPY docker.cfg buildout.cfg /plone/instance/
COPY base.cfg requirements.txt constraints_plone51.txt /plone/instance/
#COPY pypi-local  /plone/instance/pypi-local

# add resources that need to be writeable
COPY --chown=plone:plone test_plone51.cfg /plone/instance
COPY --chown=plone:plone resources  /plone/instance/resources

RUN pip install -r requirements.txt --upgrade
RUN gosu plone buildout -c docker.cfg