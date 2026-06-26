# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Awesome-ESM Documentation"
copyright = "2026 Awesome-ESM Contributors"
author = "Biohub and Awesome-ESM Community"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "myst_nb",
    "sphinx_immaterial",
    "sphinx_external_toc",
    "sphinx_design",
    "sphinxext.opengraph",  # For OpenGraph metadata
]

# Autodoc configuration
autodoc_default_options = {
    "member-order": "alphabetical",
    "exclude-members": "__init__",
}
autodoc_typehints = "none"
autodoc_class_signature = "separated"
autoclass_content = "both"

# Napoleon configuration (for Google/NumPy docstrings)
napoleon_custom_sections = ["Lifecycle"]

# Intersphinx mapping (for linking to external documentation)
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy", None),
}

# Paths and file configuration
# templates_path = ["_templates"] 
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.md"]

# External TOC
external_toc_path = "_toc.yml"
external_toc_exclude_missing = True

# MyST configuration
myst_enable_extensions = ['colon_fence']
myst_heading_anchors = 4

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_js_files = ["js/faq.js", "js/version_redirect.js"]

# html_logo = ""
html_title = "Awesome-ESM Documentation"
html_favicon = "_static/img/favicon.png"
html_theme = "sphinx_immaterial"

html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github",
        "edit": "material/file-edit-outline",
    },
    "site_url": "https://dgmccart.github.io/Awesome-ESM",
    "repo_url": "https://github.com/dgmccart/Awesome-ESM/",
    "repo_name": "Awesome-ESM",
    "edit_uri": "blob/main/docs",
    "globaltoc_collapse": False,
    "features": [
        "toc.follow",
        "toc.sticky",
        "announce.dismiss",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "custom",
            "accent": "custom",
            "toggle": {
                "icon": "material/lightbulb-outline",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "custom",
            "accent": "custom",
            "toggle": {
                "icon": "material/lightbulb",
                "name": "Switch to light mode",
            },
        },
    ],
    "font": {
        "text": "Inter",  # used for all the pages' text
        "code": "Roboto Mono",  # used for literal code blocks
    },
    "version_dropdown": False,  # Set to True if you have versioning
    
    # Disable top navigation
    "primary_sidebar": "left",  # Move sidebar to left
    "announcement": None,
    
    # Logo customization
    "logo": {
        "image_light": "_static/Biohub_white_text.png",  # Your dark mode logo
        "image_dark": "_static/Biohub_black_text.png",   # Your light mode logo
    },
    
    # Sidebar options
    "sidebar_hide_on_mobile": False,
    "navigation_with_keys": True,
}

# Remove icons from toc elements in API page
object_description_options = [
    ("py:class", dict(toc_icon_class=None)),
    ("py:parameter", dict(toc_icon_class=None, include_in_toc=False)),
    ("py:method", dict(toc_icon_class=None, include_in_toc=False)),
    ("py:attribute", dict(include_in_toc=False)),
    ("py:.*", dict(include_fields_in_toc=False)),
]

# Custom admonitions
sphinx_immaterial_custom_admonitions = [
    {
        "name": "info",
        "title": "Info",
        "color": "#6E4FF9",  # Indigo500
        "icon": "material/information",
        "override": True,
    },
    {
        "name": "warning",
        "title": "Warning",
        "color": "#E8B923",  # Warning yellow
        "icon": "material/alert",
        "override": True,
    },
]

sphinx_immaterial_icon_path = ["./_static/img"]

# OpenGraph metadata
ogp_social_cards = {
    "enable": False,  # Set to True if you want social media cards
}
ogp_site_url = "https://dgmccart.github.io/Awesome-ESM"
ogp_site_name = "Awesome-ESM Documentation"
ogp_image = "_static/img/logo.svg"

# HTML context for custom theme variables
def setup(app):
    app.add_config_value('has_custom_sidebar', True, 'html')
