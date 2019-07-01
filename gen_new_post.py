#!/usr/bin/env python
# -*- coding: utf-8 -*- #
"""
genarticle.py
-------------

Generate the skeleton of an erdos article by using jinja2 templates.
Cloned from:
https://github.com/leotrs/erdos/blob/master/scripts/templates/genarticle.py
"""

import os
import argparse
import subprocess
from collections import defaultdict
from string import punctuation
from jinja2 import Environment, FileSystemLoader


ROOT = '.'
CONTENT_DIR = os.path.join(ROOT, 'content/drafts/')
TEMPLATES_DIR = os.path.join(ROOT, '.')
TEMPLATE_FILE = 'template.md'    # must be realteive to TEMPLATES_DIR


def make_vars(**kwargs):
    """Returns a dict with var=value pairs, to be passed to the template."""
    vars_dict = defaultdict(str)
    vars_dict.update(kwargs)

    # generate dd/mm/yyyy date string
    vars_dict['date'] = subprocess.getoutput('date "+%Y-%m-%d %H:%M:%S"')


    # .. and a hyphenated version of article summary ..
    table = {ord(p): '' for p in punctuation}
    slug = vars_dict['path'].lower().translate(table).replace(' ', '-')

    vars_dict['slug'] = slug

    return vars_dict


def render(**kwargs):
    """Creates the appropriate jinja2 objects and renders the template."""
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    template = env.get_template(TEMPLATE_FILE)

    return template.render(**make_vars(**kwargs))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('path', help='the output file for the new article - '
                        'must be relative to erdos/content directory')
    parser.add_argument("-t", "--title", help="specify article title")
    parser.add_argument("-c", "--category", help="specify article category")
    parser.add_argument("-s", "--summary", help="specify article summary")
    args = parser.parse_args()

    date = subprocess.getoutput('date "+%Y-%m-%d"')
    slug = args.path.lower().replace(' ', '-')
    file_path = date + '-' + slug + '.md'
    with open(os.path.join(CONTENT_DIR, file_path), 'w+') as outfile:
        text = render(**args.__dict__)
        outfile.write(text)
        print("Create new post in %s%s" % (CONTENT_DIR, file_path))
