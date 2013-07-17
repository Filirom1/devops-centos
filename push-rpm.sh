#!/bin/bash
set -e
cd ${0%/*}

working_dir=`pwd`
tmp_dir=/tmp/filirom1/devops

rm -fr $tmp_dir
mkdir -p $tmp_dir

for dir in */; do
  echo "----> $working_dir/$dir"
  cd "$working_dir/$dir"
  source build.sh
  cp $working_dir/$dir/RPMS/**/*.rpm "$tmp_dir"
done;


cd $tmp_dir
createrepo .
git init
git add -A
git commit -m "yum repo"
git push https://Filirom1@github.com/Filirom1/devops-centos.git master:gh-pages -f


