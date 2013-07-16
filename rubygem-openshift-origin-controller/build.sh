#!/bin/bash

echo "before run:"
echo "yum install scl-utils-build ruby193-build ruby193-rubygems-devel"
echo ""

spectool --directory $PWD/SOURCES -g SPECS/*.spec
rpmbuild -bb --define="_topdir $PWD" SPECS/*.spec
