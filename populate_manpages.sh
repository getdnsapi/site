#!/bin/sh

if [ $# -ne 1 -o ! -f $1/doc/libgetdns.3 ]
then
	echo "usage: $0 <getdns src with make doc done>"
	exit
fi

for m in $1/doc/*.3
do
	name=${m#$1/doc/}
	name=${name%.3}
	if [ ! -d content/documentation/manpages/$name ]
	then
		mkdir content/documentation/manpages/$name
	fi
	( echo title: $name.3
	  echo ---
	  echo body:
	  echo ""
	  groff -mandoc -T html $m | awk 'BEGIN{p=0}/<\/body>/{p=0}{if(p==1)print}/<body>/{p=1}'
	) > content/documentation/manpages/$name/contents.lr
done

