#!/bin/sh

for f in content/releases/*/*.tar.gz*
do
	distdirfile="${f#content/releases/}"
	distfile="${f#content/releases/*/}"
	if [ ! -L "assets/dist/$distfile" ]
	then
		ln -s "../releases/$distdirfile" "assets/dist/$distfile"
	fi
done
for f in content/releases/*/*.tar.gz
do
	distfile="${f#content/releases/*/}"
	if [ ! -f "assets/dist/$distfile.sha256" ]
	then
		openssl sha256 "$f" > "assets/dist/$distfile.sha256"
	fi
done
