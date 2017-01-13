#!/bin/sh

for catdir in content/categories/*
do
	[ ! -d "$catdir" ] && continue
	cat="${catdir#content/categories/}"
	for linkpath in "$catdir"/*
	do
		link="${linkpath#$catdir/}"
		[ -f "$linkpath" -a "$link" = "contents.lr" ] && continue
		if [ ! -L "$linkpath" ]
		then
			echo "Error: \"$linkpath\" is not a symbolic link"
			exit 1
		fi
		if [ ! -e "$linkpath"/contents.lr ]
		then
			echo "Source of \"$linkpath\" has been removed. Removing..."
			rm "$linkpath"
		elif ! grep -q "^categories: .*$cat" "$linkpath"/contents.lr
		then
			echo "Source of \"$linkpath\" does not have category \"$cat\" anymore. Removing..."
			rm "$linkpath"
		fi
	done
	for postcontent in `grep -l "^categories: .*$cat" content/blog/*/contents.lr`
	do
		postdir="${postcontent%/contents.lr}"
		post="${postdir#content/blog/}"
		if [ ! -L "$catdir/$post" ]
		then
			if [ -x $catdir/$post ]
			then
				echo "Error: \"$catdir/$post\" exists, but is not a symbolic link"
				exit 1
			else
				echo "Adding new link for post \"$post\" in category \"$cat\"."
				ln -s "../../blog/$post" "$catdir/$post"
			fi
		fi
	done
done
