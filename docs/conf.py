# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "gbmgeometry"
copyright = "2020, J. Michael Burgess"
author = "J. Michael Burgess"


import sys
import os

from pathlib import Path

import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath("../"))

DOCS = Path(__file__).parent

# -- Generate API documentation ------------------------------------------------
def run_apidoc(app):
    """Generage API documentation"""
    import better_apidoc

    better_apidoc.APP = app
    better_apidoc.main(
        [
            "better-apidoc",
            # "-t",
            # str(docs / "_templates"),
            "--force",
            "--no-toc",
            "--separate",
            "-o",
            str(DOCS / "API"),
            str(DOCS / ".." / "gbmgeometry"),
        ]
    )


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    "nbsphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
    "sphinx.ext.githubpages",
    "sphinx.ext.napoleon",
#    "rtds_action",
]


napoleon_google_docstring = True
napoleon_use_param = True
napoleon_include_private_with_doc = True
napoleon_include_init_with_doc = True


autodoc_default_options = {
    'members': 'var1, var2',
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}



# # The name of your GitHub repository
# rtds_action_github_repo = "grburgess/gbmgeometry"


# # The path where the artifact should be extracted
# # Note: this is relative to the conf.py file!
# rtds_action_path = "notebooks"

# # The "prefix" used in the `upload-artifact` step of the action
# rtds_action_artifact_prefix = "notebooks-for-"

# # A GitHub personal access token is required, more info below
# rtds_action_github_token = os.environ["GITHUB_TOKEN"]


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]


# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

autosectionlabel_prefix_document = True

# avoid time-out when running the doc

nbsphinx_timeout = 30 * 60

# nbsphinx_execute_arguments = [
#     "--InlineBackend.figure_formats={'svg', 'pdf'}",
#     "--InlineBackend.rc={'figure.dpi': 96}",
# ]

autodoc_member_order = "bysource"

autoclass_content = "both"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
# html_theme = 'lsst_dd_rtd_theme'
# htm_theme_path = [sphinx_pdj_theme.get_html_theme_path()]
# Output file base name for HTML help builder.
htmlhelp_basename = "gbmgeometrydoc"



# The name of the Pygments (syntax highlighting) style to use.
# The light-dark theme toggler overloads this, but set default anyway
pygments_style = 'none'

# Create local pygments copies
# Previously used: https://github.com/richleland/pygments-css
# But do not want to depend on some random repository
from pygments.formatters import HtmlFormatter  # noqa: E402
from pygments.styles import get_all_styles  # noqa: E402
path = os.path.join('_static', 'pygments')
if not os.path.isdir(path):
    os.mkdir(path)
for style in get_all_styles():
    path = os.path.join('_static', 'pygments', style + '.css')
    if os.path.isfile(path):
        continue
    with open(path, 'w') as f:
        f.write(HtmlFormatter(style=style).get_style_defs('.highlight'))


html_theme_options = {
    'logo_only':False,
    'display_version': False,
    'collapse_navigation': True,
    'navigation_depth': 4,
    'prev_next_buttons_location': 'bottom',  # top and bottom
}


html_logo = "media/logo.png"
html_show_sourcelink = False
html_favicon = "media/favicon.ico"

html_show_sphinx = False





# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
# html_css_files = [
#     "css/custom.css",
    
# ]


# html_js_files = [
#     'css/custom.js',
# ]


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


master_doc = "index"

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "gbmgeometry.tex",
        u"gbmgeometry Documentation",
        u"J. Michael Burgess",
        "manual",
    ),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "gbmgeometry", u"gbmgeometry Documentation", [author], 1)]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "gbmgeometry",
        u"gbmgeometry Documentation",
        author,
        "gbmgeometry",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# -----------------------------------------------------------------------------
# def setup(app):
#     app.connect("builder-inited", run_apidoc)


#    app.connect("builder-inited", generate_patched_readme)
