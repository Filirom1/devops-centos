#!/bin/bash

#git clone https://github.com/worldline/openshift-origin-server
#cd openshift-origin-server
#git branch --set-upstream openshift-origin-release-3 origin/openshift-origin-release-3
#git branch --set-upstream worldline-openshift-origin-release-3 origin/worldline-openshift-origin-release-3

#git checkout worldline-openshift-origin-release-3

for name in broker controller console; do
  cd $name
  git diff --binary  --relative openshift-origin-release-3 worldline-openshift-origin-release-3 -- . > ../$name.patch
  cd -
done

