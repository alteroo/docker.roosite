#!/bin/bash

if [ -z $(which git-lfs) ]; then \
    sudo apt-get install software-properties-common -y
    sudo add-apt-repository ppa:git-core/ppa -y
    curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
    sudo apt-get install git-lfs
fi

if [ ! -e "content" ]; then \
    git clone git@gitlab.com:alteroo/ccrp/ccrp.data.git content
fi
cd content
git lfs pull master
tar -xzvf content.tgz
rm content.tgz
cd ..
sleep 10
bin/instance run scripts/addSite.py $1
sleep 30
bin/instance run scripts/importer.py $1
cd content
rm -rf *.json
git checkout content.tgz
cd ..
