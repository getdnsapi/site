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
	distdir="${f%$distfile}"
	if [ ! -f "assets/dist/$distfile.sha256" ]
	then
		(
			cd "$distdir"
			openssl sha256 "$distfile" > "../../../assets/dist/$distfile.sha256"
		)
	fi
	if [ ! -f "assets/dist/$distfile.sha1" ]
	then
		(
			cd "$distdir"
			openssl sha1 "$distfile" > "../../../assets/dist/$distfile.sha1"
		)
	fi
	if [ ! -f "assets/dist/$distfile.md5" ]
	then
		(
			cd "$distdir"
			openssl md5 "$distfile" > "../../../assets/dist/$distfile.md5"
		)
	fi
done
