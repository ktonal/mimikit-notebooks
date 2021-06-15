#!/bin/bash

#pip install nbformat mimikit

git checkout main

python make_notebooks.py

# grab mimikit version
export TAG="v$(pip list | grep mimikit |  awk '{print $2}')"

# delete tag if it already exists
if [ "$(git tag -l $TAG)" ]; then
    git tag -d $TAG
fi

# add, commit, tag, push

git add .

git commit -m $TAG

git tag -a $TAG -m $TAG

git push

