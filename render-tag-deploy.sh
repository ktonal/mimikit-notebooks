#!/bin/bash

pip install nbformat mimikit

git checkout test

python make_notebooks.py

# grab mmk version
export TAG="v$(pip list | grep mimikit |  awk '{print $2}')"

if [ "$(git tag -l $TAG)" ]; then
    git tag -d $TAG

fi
git commit -am $TAG

git tag -a $TAG -m $TAG

#git push

