#!/usr/bin/env python

import os
import github3
from pprint import pprint
import tempfile
import subprocess

def parse_lektor(lr):
	d = dict()
	for a in lr.strip().split('---\n'):
		lns = a.strip().split('\n')
		if len(lns) == 1:
			key, value = lns[0].split(': ')
		else:
			key = lns[0][:-1]
			value = '\n'.join(lns[2:])
		d[key.strip()] = value.strip()
	return d

def new_release(tag):
	global repo

	dn  = 'content/releases/getdns-' + tag[1:].replace('.', '-')
	with file(dn + '/contents.lr') as f:
		contents = parse_lektor(f.read())
	version = contents['version']
	dversion = contents['version'].replace('.', '-')
	sha256 = contents['sha256']
	announcement = """&nbsp; | <div align="left">Please do not use the github generated Source code (zip) and (tar.gz) files, but our own tarball instead:</div>
------- | ------------------------
tarball | <https://getdnsapi.net/dist/getdns-%s.tar.gz>
pgp sig | <https://getdnsapi.net/dist/getdns-%s.tar.gz.asc>
sha256  | %s

""" % ( version, version, sha256.strip() )

	if 'image' in contents and contents['image'].strip():
		img_parts = contents['image'].split('.')
		image180 = '.'.join(img_parts[:-1]) + '@180' + '.' + img_parts[-1]
		announcement += '\n<img align="right" ' \
		              + 'src="https://getdnsapi.net/releases/getdns-%s/%s">\n\n' \
		              % (dversion, image180)

	with tempfile.NamedTemporaryFile() as f:
		f.write(contents['announcement']
		       .replace(']: /', ']: https://getdnsapi.net/')
		       .replace('](/' , '](https://getdnsapi.net/')
		       .replace('\n  * ', '\n  - ')
		       )
		tmpfn = f.name
		f.flush()
		f.seek(0)
		announcement += subprocess.check_output(['pandoc', '-f', 'markdown', '-t', 'markdown', '--wrap', 'preserve'], stdin=f).replace(' &gt; ', '\n    > ')

	announcement += "\n### ChangeLog\n\n```\n%s\n```\n" % contents['changelog']
	if 'stubbychangelog' in contents and contents['stubbychangelog'].strip():
		announcement += "\n### Stubby ChangeLog\n\n```\n%s\n```\n" % contents['stubbychangelog']

	if 'title' in contents:
		title = contents['title']
	elif 'rc' not in version and 'a' not in version and 'b' not in version:
		title = 'getdns-%s release' % version
	else:
		raise(Exception('No title!'))

	rel = repo.create_release( tag_name = tag
	                         , name = title
	                         , body = announcement
	                         , draft = True
	                         , prerelease = 'rc' in version
	                         )
	with file(dn + '/getdns-%s.tar.gz' % version) as f:
		rel.upload_asset( content_type = 'application/gzip'
		                , name = 'getdns-%s.tar.gz' % version
		                , asset = f
		                )
	with file(dn + '/getdns-%s.tar.gz.asc' % version) as f:
		rel.upload_asset( content_type = 'test/plain'
		                , name = 'getdns-%s.tar.gz.asc' % version
		                , asset = f
		                )

# using username and password
with file(os.environ.get('HOME', '~') + '/.github/auth') as f:
	g = github3.login(*[x.strip() for x in f.read().strip().split()[:2]])

repo = g.repository('getdnsapi', 'getdns')
rels = dict()

for rel in repo.iter_releases():
	rels[rel.tag_name] = rel

for tag in repo.iter_tags():
	if not tag.name.startswith('v'):
		continue
	if tag.name in rels:
		print 'update', rels[tag.name]
	elif not os.path.exists('content/releases/getdns-%s/contents.lr' % tag.name[1:].replace('.', '-')):
		print 'skipping content/releases/getdns-%s/contents.lr' % tag.name[1:].replace('.', '-')
		continue
	else:
		print 'new release for', tag.name
		new_release(tag.name)
		break
