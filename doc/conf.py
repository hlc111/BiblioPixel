#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# BiblioPixel documentation build configuration file, created by
# sphinx-quickstart on Mon Sep 10 13:03:18 2018.
#
import os, sys
sys.path.insert(0, os.path.abspath('..'))


# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.extlinks',
    'sphinx.ext.githubpages',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
#    'sphinxcontrib.fulltoc',
    ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:\
#
source_suffix = ['.rst']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'BiblioPixel'
copyright = '2018-2019, Maniacal Labs, Inc and Tom Ritchford'
author = 'Maniacal Labs, Inc and Tom Ritchford'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
import bibliopixel
version = bibliopixel.VERSION
# The full version, including alpha/beta/rc tags.
release = bibliopixel.VERSION

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

_IMAGE_DIR = """https://raw.githubusercontent.com/ManiacalLabs/DocsFiles\
/master/BiblioPixel/doc/"""

# Patterns to replace in every RST file
rst_prolog = '.. |ImageDir| replace:: %s\n' % _IMAGE_DIR


# -- Options for HTML output ----------------------------------------------

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
alabaster_html_theme_options = {
    'show_related': True,
    'github_user': 'ManiacalLabs',
    'github_repo': 'BiblioPixel',
    'github_banner': True,
    'github_button': True,
    'travis_button': True,
    'show_powered_by': False,
    }

sphinx_rtd_html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
#    'vcs_pageview_mode': '',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

if not True:
    html_theme = 'alabaster'
    html_theme_options = alabaster_html_theme_options
else:
    html_theme = 'sphinx_rtd_theme'
    html_theme_options = sphinx_rtd_html_theme_options

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',
        'searchbox.html',
        'globaltoc.html',
        'sourcelink.html',
    ]
}

show_relbars = True
show_related = True

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'BiblioPixelDoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'BiblioPixel.tex', 'BiblioPixel Documentation',
     'Maniacal Labs, Inc', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'bibliopixel', 'BiblioPixel Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'BiblioPixel', 'BiblioPixel Documentation',
     author, 'BiblioPixel', 'One line description of project.',
     'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}


# -- Options for extlinks output -------------------------------------------
extlinks = {
    'ImageDir': (_IMAGE_DIR + '%s', None)
}
