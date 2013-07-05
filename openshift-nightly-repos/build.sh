#!/bin/bash

rpmbuild -bb --define="_topdir $PWD" SPECS/*.spec
