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

project = 'Leetcode Solutions'
copyright = '2022, Prakash Sellathurai'
author = 'Prakash Sellathurai'
html_title = 'Leetcode Solutions'
# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}


myst_enable_extensions = [
    "amsmath",        # Enables LaTeX math equations
    "colon_fence",    # Allows using ::: instead of ``` for blocks
    "deflist",        # Enables definition lists
    "dollarmath",     # Enables $math$ and $$math$$ syntax
    "fieldlist",      # Enables reStructuredText-style field lists
    "html_admonition",# Allows HTML <div class="admonition"> tags
    "html_image",     # Parses HTML <img> tags automatically
    "linkify",        # Automatically converts bare URLs to hyperlinks
    "replacements",   # Enables text shortcuts (e.g., (c) becomes ©)
    "smartquotes",    # Converts straight quotes to curly quotes
    "substitution",   # Enables global text substitutions
    "tasklist",       # Enables GitHub-style - [ ] task lists
]

myst_heading_anchors = 3

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ "myst_parser", 'sphinx_immaterial']


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_immaterial'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []


# material theme options (see theme.conf for more information)
html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github",
        "edit": "material/file-edit-outline",
    },
    "site_url": "https://prakashsellathurai.com/leetcode-solutions/",
    "repo_url": "https://github.com/prakashsellathurai/leetcode-solutions/",
    "repo_name": "leetcode-solutions",
    "edit_uri": "blob/main",
    "globaltoc_collapse": True,
    "features": [
        "navigation.expand",
        # "navigation.tabs",
        # "navigation.tabs.sticky",
        # "toc.integrate",
        "navigation.sections",
        # "navigation.instant",
        # "header.autohide",
        "navigation.top",
        "navigation.footer",
        # "navigation.tracking",
        # "search.highlight",
        "search.share",
        "search.suggest",
        "toc.follow",
        "toc.sticky",
        "content.tabs.link",
        "content.code.copy",
        "content.action.edit",
        "content.action.view",
        "content.tooltips",
        "announce.dismiss",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme)",
            "toggle": {
                "icon": "material/brightness-auto",
                "name": "Switch to light mode",
            },
        },
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "slate",
            "primary": "light-green",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/lightbulb",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "default",
            "primary": "deep-orange",
            "accent": "lime",
            "toggle": {
                "icon": "material/lightbulb-outline",
                "name": "Switch to system preference",
            },
        },
    ],
    # BEGIN: version_dropdown
    "version_dropdown": False,
    "version_info": [

    ],
    # END: version_dropdown
    "toc_title_is_page_title": True,
    # BEGIN: social icons
    "social": [
        {
            "icon": "fontawesome/brands/github",
            "link": "https://github.com/prakashsellathurai/leetcode-solutions",
            "name": "Source on github.com",
        },
        {
            "icon": "fontawesome/brands/python",
            "link": "https://pypi.org/project/slough/",
        },
    ],
    # END: social icons
}