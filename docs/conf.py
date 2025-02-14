# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DistilRLIntro'
copyright = '2025, Youxiang Dong'
author = 'Youxiang Dong'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'myst_parser',
    'sphinx.ext.mathjax',
    #  'sphinx_math_dollar',
]

myst_enable_extensions = [
    "dollarmath",
    "colon_fence",  # for supporting ::: directives
    "linkify",      # for automatic link detection
    "substitution", # for substitutions
    "deflist",      # for definition lists
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}

myst_heading_anchors = 3

html_static_path = ['_static']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
