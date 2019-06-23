FROM registry.gitlab.com/alteroo/carimac.com.buildout:2017-11-17-1519

ENV buildDeps="git wget sudo python-setuptools python-dev build-essential libssl-dev libxml2-dev libxslt1-dev libbz2-dev libjpeg62-turbo-dev libtiff5-dev libopenjp2-7-dev" 
ENV runDeps="libxml2 libxslt1.1 libjpeg62 rsync lynx wv libtiff5 libopenjp2-7 poppler-utils"


COPY site.cfg /plone/instance/
COPY profile  /plone/instance/profile
COPY pypi-local  /plone/instance/pypi-local
COPY src /plone/instance/src
COPY resources  /plone/instance/resources


USER root
RUN apt-get update \
 && apt-get install -y --no-install-recommends $buildDeps  \
 && chown -R plone:plone /plone /data 

USER plone
RUN bin/buildout -c site.cfg

USER root
RUN SUDO_FORCE_REMOVE=yes apt-get remove --purge -y $buildDeps\
 && apt-get install -y --no-install-recommends $runDeps \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf /plone/buildout-cache/downloads/* \
 && rm -rf /plone/Plone-docs \
 && find /plone \( -type f -a -name '*.pyc' -o -name '*.pyo' \) -exec rm -rf '{}' +

USER plone
