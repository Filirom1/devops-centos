#!/bin/bash
cd ${0%/*}

spectool --directory $PWD/SOURCES -g SPECS/*.spec
rpmbuild -bb --define="_topdir $PWD" SPECS/*.spec
