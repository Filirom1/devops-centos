#!/bin/bash

declare -A urls
urls[broker]="https://mirror.openshift.com/pub/openshift/release/3/rhel-6/packages/SRPMS/openshift-origin-broker-1.15.1.2-1.el6.src.rpm"
urls[controller]="https://mirror.openshift.com/pub/openshift/release/3/rhel-6/packages/SRPMS/rubygem-openshift-origin-controller-1.18.0.1-1.el6.src.rpm"
urls[console]="https://mirror.openshift.com/pub/openshift/release/3/rhel-6/packages/SRPMS/rubygem-openshift-origin-console-1.18.0.1-1.el6.src.rpm"

for name in broker controller console; do
  curl "${urls[$name]}" > $name.src.rpm
  rpm2cpio $name.src.rpm | cpio -ivd
  rm -f *.tar.gz
done;

