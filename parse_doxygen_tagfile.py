#!/usr/bin/env python

import xml.etree.ElementTree as ET
import sys, os

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("usage: %s <tagfile>" % sys.argv[0])
		sys.exit(1)
	tree = ET.parse(sys.argv[1])
	root = tree.getroot()
	for member in root.iter('member'):
		name = member.find('name').text
		if '(' in name:
			continue
		anchorfile = member.find('anchorfile').text
		anchor = member.find('anchor').text
		link = anchorfile + '#' + anchor
		title = name
		args = member.find('arglist').text
		if args:
			title += args
		typ = member.find('type')
		if typ is not None and typ.text is not None:
			title = typ.text + ' ' + title
		try:
			os.mkdir('content/functions/%s' % name)
		except OSError:
			pass
		with file('content/functions/%s/contents.lr' % name, 'w') as f:
			f.write("""_model: link
---
_slug: %s.html
---
title: %s
---
link: /doxygen/1.1.0/%s
""" % (name, title, link))
