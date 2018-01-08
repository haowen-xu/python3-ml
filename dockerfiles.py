#!/usr/bin/env python
import codecs
import os

from jinja2 import Environment, FileSystemLoader

source_root = os.path.split(os.path.abspath(__file__))[0]
env = Environment(loader=FileSystemLoader(source_root))
template = env.get_template('Dockerfile.template')

for name in ('cpu', 'gpu'):
    with codecs.open(os.path.join(source_root, name, 'Dockerfile'), 'wb', 'utf-8') as f:
        f.write(template.render(gpu=name == 'gpu') + '\n')
