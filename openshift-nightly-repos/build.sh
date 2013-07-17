#!/bin/bash
cd ${0%/*}

rpmbuild -bb --define="_topdir $PWD" SPECS/*.spec
