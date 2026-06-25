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
# templates_path = ["_templates"] # removed _templates folder due to it overriding the theme
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

/* ==========================================================================
   Biohub Sidebar
   ========================================================================== */

/* Remove top navigation */
.md-tabs {
  display: none;
}

/* Sidebar */
.md-sidebar--primary {
  width: 280px;
  background: var(--gray-200);
  border-right: 1px solid #D5D5D5;
}

.md-sidebar__scrollwrap {
  background: var(--gray-200);
}

.md-nav {
  background: transparent;
}

/* Sidebar header */
.md-sidebar-brand {
  display: flex;
  align-items: center;
  gap: 12px;

  padding: 18px 20px;

  border-bottom: 1px solid #D5D5D5;
}

.md-sidebar-brand img {
  height: 34px;
  width: auto;
}

.md-sidebar-brand span {
  font-size: 22px;
  font-weight: 600;
  color: var(--black);
}

/* Hide/show logos automatically */
.logo-dark {
  display: none;
}

[data-md-color-scheme="slate"] .logo-light {
  display: none;
}

[data-md-color-scheme="slate"] .logo-dark {
  display: block;
}

/* Navigation */
.md-nav__link {
  display: flex;
  align-items: center;
  gap: 12px;

  color: var(--gray-600);
  font-size: 14px;
  font-weight: 500;

  padding: 10px 18px;

  border-radius: 10px;

  transition: all .15s ease;
}

.md-nav__link:hover {
  background: var(--indigo-100);
  color: var(--indigo-500);
}

.md-nav__item--active > .md-nav__link {
  background: var(--indigo-100);
  color: var(--indigo-500);
  font-weight: 600;
}

/* Second level */
.md-nav__list .md-nav__list {
  margin-left: 16px;
}

.md-nav__list .md-nav__list .md-nav__link {
  font-size: 13px;
}

/* Collapse button */
.md-sidebar-collapse {
  position: absolute;
  top: 18px;
  right: 16px;

  width: 32px;
  height: 32px;

  border-radius: 8px;
  border: 1px solid var(--gray-200);

  display: flex;
  align-items: center;
  justify-content: center;

  cursor: pointer;

  background: white;
}

.md-sidebar-collapse:hover {
  background: var(--indigo-100);
}

/* Main content spacing */
.md-main__inner {
  margin-left: 300px;
}

/* Remove breadcrumbs */
.md-path,
.md-breadcrumbs,
.md-content__button {
  display: none !important;
}
