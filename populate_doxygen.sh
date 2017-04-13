#!/bin/sh

if [ $# -ne 1 -o ! -f $1/doc/libgetdns.3 -o ! -f $1/src/Doxyfile ]
then
	echo "usage: $0 <getdns src with make doc done>"
	exit
fi

TEMPLATESDIR=`lektor project-info --output-path`/doxygen-templates
DOXYCONFIG=`mktemp`
PROJECT_NUMBER=`grep ^PROJECT_NUMBER $1/src/Doxyfile|sed 's/^[^=]*=[ 	]*//g'`
echo $DOXYCONFIG
(
	egrep -v '^HTML_HEADER|^HTML_FOOTER|^HTML_EXTRA_FILES|OUTPUT_DIRECTORY|GENERATE_LATEX|GENERATE_MAN' $1/src/Doxyfile
	echo HTML_HEADER=$TEMPLATESDIR/header.html
	echo HTML_FOOTER=$TEMPLATESDIR/footer.html
	echo HTML_EXTRA_FILES=$TEMPLATESDIR/doxy-boot.js
	echo OUTPUT_DIRECTORY=`pwd`/assets/doxygen/
	echo GENERATE_LATEX=NO
	echo GENERATE_MAN=NO
	#echo HTML_OUTPUT=$PROJECT_NUMBER
	echo HTML_OUTPUT=.
) > $DOXYCONFIG && (
	cd $1/src
	doxygen $DOXYCONFIG
)
