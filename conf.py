# -*- coding: utf-8 -*-

import sys
import os

sys.path.append(os.path.join('..', 'sphinx-template'))
from utils import get_year

# -- General configuration ------------------------------------------------

# General information about the project.
project = u'Školení PostGIS pro začátečníky'
#copyright = u'2014, Martin Landa (GISMentors.eu)'
copyright = u'2014-%d, Jan JELEN Michálek a Martin Landa (GISMentors.eu)' % get_year()

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.6'
# The full version, including alpha/beta/rc tags.
release = '%sbeta' % version

# -- Options for HTML output ----------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'skoleni-postgis-zacatecnik'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project

# -- Options for LaTeX output ---------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', '%s-%s.tex' % (htmlhelp_basename, version), project,
     u'GISMentors', u'manual'),
    ]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', htmlhelp_basename, project,
     [copyright], 1)
    ]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', htmlhelp_basename, project,
     copyright, htmlhelp_basename, project,
     'Miscellaneous'),
    ]

sys.path.append(os.path.join('..', 'sphinx-template'))
from conf_base import *
